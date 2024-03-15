#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ocpp.charge_point import (
    camel_to_snake_case, snake_to_camel_case, remove_nones)
from ocpp.v16.datatypes import MeterValue, SampledValue
from ocpp.v16 import call_result
from ocpp.v16.enums import Action, MessageTrigger, UnlockStatus, ChargingRateUnitType, UpdateType, RegistrationStatus, ConfigurationStatus, AvailabilityStatus, DeleteCertificateStatus, GetInstalledCertificateStatus, AvailabilityType, ClearCacheStatus, UpdateStatus, ClearChargingProfileStatus, ChargePointStatus, AuthorizationStatus, RemoteStartStopStatus, UpdateFirmwareStatus, LogStatus, UploadLogStatus, TriggerMessageStatus, CertificateSignedStatus, CertificateStatus, ResetType
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.call import (BootNotificationPayload, MeterValuesPayload, LogStatusNotificationPayload, GetLogPayload, ExtendedTriggerMessagePayload, ClearCachePayload, ChangeConfigurationPayload, ChangeAvailabilityPayload, CancelReservationPayload,
                           GetConfigurationPayload)
from ocpp.v16 import call
from ocpp.routing import on, after, create_route_map
from typing import Dict, List, Optional
from dataclasses import asdict, is_dataclass
from datetime import datetime, timedelta
import logging
import asyncio
import wx
import threading
import requests
# -----------------------------
import wxasync
import OCPP_CS_GUIv4_2024
# ---------------------------------
import string
import os
import time
# import datetime
from time import sleep
import sys
import subprocess
import win32pipe
import win32file
import importlib

# import pyshark
# SSL
import pathlib
import ssl

from glob import *
# from PIL import Image
import winsound
importlib.reload(sys)
# sys.setdefaultencoding('utf8')
# ocpp
# -------------------
try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)
# ocpp2


# -------------------

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    def __init__(self, CP_id, ws, window):
        cp.__init__(self, CP_id, ws)
        self.window = window
        global CS_StatusNotification_S
        CS_StatusNotification_S = 'Available'
        self.ws = ws

    @on(Action.BootNotification)
    def on_boot_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
        self.window.LogMessage2(charge_point_vendor)
        self.window.m_textCtrl91.SetValue(charge_point_vendor)
        self.window.m_textCtrl4.SetValue(charge_point_model)
        self.window.LogMessage2(charge_point_model)
        # self.window.LogMessage2(kwargs['charge_point_serial_number'])
        # self.window.LogMessage2(kwargs['charge_box_serial_number'])
        # self.window.m_textCtrl81.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.window.m_textCtrl6.SetValue('CP BootNotification')
        return call_result.BootNotificationPayload(
            current_time=datetime.strftime(
                datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"),
            # current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted
        )

    @on(Action.StatusNotification)
    def on_StatusNotification(self, **kwargs):
        self.window.m_textCtrl6.SetValue(kwargs['status'])
        self.window.LogMessage1('Receive [CP Status]:'+kwargs['status'])
        self.window.LogMessage1('CP connector_id:'+str(kwargs['connector_id']))
        self.window.LogMessage1('CP error_code:'+kwargs['error_code'])
        # self.window.LogMessage2(kwargs['timestamp'])
        return call_result.StatusNotificationPayload()

    @on(Action.Heartbeat)
    def on_Heartbeat(self, **kwargs):
        # print("TC_on_Heartbeat.")
        self.window.LogMessage1(
            'Heartbeat:'+str(datetime.utcnow().isoformat()))
        # self.window.m_textCtrl81.SetBackgroundColour(wx.Colour(0, 255, 0))
        # self.window.m_textCtrl6.SetValue('CP Heartbeat')
        return call_result.HeartbeatPayload(current_time=datetime.strftime(datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"))

    @on(Action.Authorize)
    def on_Authorize(self, **kwargs):
        # print("TC_on_Authorize.")
        self.window.LogMessage1('id_tag:'+kwargs['id_tag'])
        id_tag_info1 = {}
        id_tag_info1['status'] = AuthorizationStatus.accepted
        # "04B0267AE05C87":
        if kwargs['id_tag'] == self.window.m_comboBox5.Value:
            id_tag_info1['status'] = AuthorizationStatus.accepted
        elif self.window.m_comboBox5.Value == 'expired':
            id_tag_info1['status'] = AuthorizationStatus.expired
        elif self.window.m_comboBox5.Value == 'blocked':
            id_tag_info1['status'] = AuthorizationStatus.blocked
        else:
            id_tag_info1['status'] = AuthorizationStatus.invalid
        self.window.LogMessage2(
            'Send[Authorize_status]:'+id_tag_info1['status'])
        return call_result.AuthorizePayload(id_tag_info=id_tag_info1)

    @on(Action.StartTransaction)
    def on_StartTransaction(self, **kwargs):
        # print("TC_on_StartTransaction.")
        self.window.m_textCtrl6.SetValue('StartTransaction')
        self.window.LogMessage1('Receive:StartTransaction')
        self.window.LogMessage1('connector_id:'+str(kwargs['connector_id']))
        self.window.LogMessage1('id_tag:'+kwargs['id_tag'])
        self.window.LogMessage1('meter_start'+str(kwargs['meter_start']))
        self.window.m_textCtrl11.SetValue(str(kwargs['meter_start']))
        self.window.LogMessage1('timestamp'+kwargs['timestamp'])
        # self.window.LogMessage1('reservation_id'+str(kwargs['reservation_id']))
        id_tag_info1 = {}
        if kwargs['id_tag'] == self.window.m_comboBox5.Value:
            id_tag_info1['status'] = AuthorizationStatus.accepted
        else:
            id_tag_info1['status'] = AuthorizationStatus.invalid
        self.window.LogMessage2(
            'Send[StartTransaction_status]:'+id_tag_info1['status'])
        self.window.LogMessage2(
            'Send[transaction_id]:'+self.window.m_textCtrl10.Value)
        return call_result.StartTransactionPayload(transaction_id=int(self.window.m_textCtrl10.Value), id_tag_info=id_tag_info1)

    @on(Action.MeterValues)
    def on_MeterValues(self, **kwargs):
        self.window.m_textCtrl6.SetValue('MeterValues')
        self.window.LogMessage1('Receive:MeterValues')
        self.window.LogMessage1('connector_id:'+str(kwargs['connector_id']))
        self.window.LogMessage1('meterValue'+str(kwargs['meter_value']))
        self.window.LogMessage1('meterValue'+str(kwargs['meter_value'][0]))
        self.window.LogMessage1(
            'meterValue'+str(kwargs['meter_value'][0]['sampled_value']))
        # {}用字典型式['XXX']，[]使用index型式[0..]
        self.window.LogMessage1('transaction_id'+str(kwargs['transaction_id']))
        return call_result.MeterValuesPayload()

    @on(Action.StopTransaction)
    def on_StopTransaction(self, **kwargs):
        # print("TC_on_StopTransaction.")
        self.window.m_textCtrl6.SetValue('StopTransaction')
        self.window.LogMessage1('Receive:StopTransaction')
        self.window.LogMessage1('reason:'+kwargs['reason'])
        self.window.LogMessage1('id_tag:'+kwargs['id_tag'])
        self.window.LogMessage1('meter_stop'+str(kwargs['meter_stop']))
        self.window.m_textCtrl12.SetValue(str(kwargs['meter_stop']))
        self.window.LogMessage1('timestamp'+kwargs['timestamp'])
        self.window.LogMessage1('transaction_id'+str(kwargs['transaction_id']))
        id_tag_info1 = {}
        if kwargs['id_tag'] == self.window.m_comboBox5.Value:
            id_tag_info1['status'] = AuthorizationStatus.accepted
        else:
            id_tag_info1['status'] = AuthorizationStatus.invalid
        self.window.LogMessage2(
            'Send[StopTransaction_status]:'+id_tag_info1['status'])
        self.window.LogMessage2(
            'Send[transaction_id]:'+self.window.m_textCtrl10.Value)
        return call_result.StopTransactionPayload(id_tag_info=id_tag_info1)

    @on(Action.CancelReservation)
    async def Send_CancelReservation(self, re_id):
        self.window.LogMessage2('Send [CancelReservation]')
        request = call.CancelReservationPayload(reservation_id=re_id)
        response = await self.call(request)
        self.window.LogMessage1('Receive [CancelReservation]' + response)

    @on(Action.ChangeConfiguration)
    async def Send_ChangeConfiguration(self, c_key, c_value):
        self.window.LogMessage2('Send [ChangeConfiguration]')
        request = call.ChangeConfigurationPayload(key=c_key, value=c_value)
        response = await self.call(request)
        if response == None:
            pass
        else:
            self.window.LogMessage1(
                'Receive [ChangeConfiguration]' + response.status)

    @on(Action.ChangeAvailability)
    async def Send_ChangeAvailability(self, con_id):
        self.window.LogMessage2('Send [ChangeAvailability]')
        request = call.ChangeAvailabilityPayload(
            connector_id=con_id, type=AvailabilityType.inoperative)
        response = await self.call(request)
        self.window.LogMessage1('Receive [ChangeAvailability]' + response)

    @on(Action.FirmwareStatusNotification)
    def on_FirmwareStatusNotification(self, **kwargs):
        # print("TC_on_Heartbeat.")
        self.window.LogMessage1(
            'FirmwareStatusNotification[status]:'+kwargs['status'])
        # self.window.m_textCtrl81.SetBackgroundColour(wx.Colour(0, 255, 0))
        # self.window.m_textCtrl6.SetValue('CP Heartbeat')
        return call_result.FirmwareStatusNotificationPayload()

    @on(Action.UpdateFirmware)
    async def Send_FirmwareUpdate(self, F_urls):
        self.window.LogMessage2('Send [FirmwareUpdate]')
        # "retrieveDate": "2024-01-15T15:02:52Z"
        request = call.UpdateFirmwarePayload(F_urls, retrieve_date=datetime.strftime(
            datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"))
        response = await self.call(request)
        if response == None:
            print('no response')
        else:
            self.window.LogMessage1('Receive [FirmwareUpdate]' + response)

    @on(Action.GetLocalListVersion)
    async def Send_Get_Local_List(self):
        self.window.LogMessage2('Send [Get_Local_List]')
        request = call.GetLocalListVersionPayload()
        response = await self.call(request)
        self.window.LogMessage1(
            'Receive [Get_Local_List]' + str(response.list_version))

    @on(Action.SendLocalList)
    async def Send_Local_Authorization(self, up_type):
        self.window.LogMessage2('Send [SendLocalList]')
        list_v = 1
        if up_type == 'Full':
            request = call.SendLocalListPayload(
                list_version=list_v, update_type=UpdateType.full)
        else:
            request = call.SendLocalListPayload(
                list_version=list_v, update_type=UpdateType.differential)
        response = await self.call(request)
        if response == None:
            pass
        else:
            self.window.LogMessage1(
                'Receive [SendLocalList]' + str(response.list_version))

    @on(Action.GetConfiguration)
    async def Send_GetConfiguration(self, key_value):
        self.window.LogMessage2('Send [GetConfiguration]')
        if key_value == '':
            request = call.GetConfigurationPayload()
            response = await self.call(request)
            r1 = response.configuration_key
            self.window.LogMessage1(
                'Receive [All GetConfiguration]')
            for keyData in r1:
                # print(keyData)
                print(keyData['key'])
                self.window.m_comboBox10.Append(keyData['key'])
        else:
            # payload = [{"key": key_value}]
            request = call.GetConfigurationPayload(
                key=[key_value])
            response = await self.call(request)
            if response == None:
                pass
            else:
                print(response)
                print(response.configuration_key)
                self.window.LogMessage1(
                    'Receive [GetConfiguration]' + response.configuration_key[0]['key'])

    @on(Action.GetDiagnostics)
    async def Send_GetDiagnostics(self):
        self.window.LogMessage2('Send [CGetDiagnostics]')
        # starttime currient time -one week
        # stop time currient time -10min
        request = call.GetDiagnosticsPayload(
            location=self.window.m_textCtrl21.Value, retries=1, retry_interval=30, start_time=datetime.strftime(
                datetime.utcnow()-timedelta(weeks=1), "%Y-%m-%dT%H:%M:%SZ"), stop_time=datetime.strftime(
                datetime.utcnow()-timedelta(minutes=10), "%Y-%m-%dT%H:%M:%SZ"))
        response = await self.call(request)
        if response == None:
            print('No response or message error')
        else:
            self.window.LogMessage1(
                'Receive [GetDiagnostics]' + response.file_name)

    @on(Action.DiagnosticsStatusNotification)
    def on_DiagnosticsStatusNotification(self, **kwargs):
        # print("TC_on_Heartbeat.")
        self.window.LogMessage1(
            'DiagnosticsStatusNotification[status]:'+kwargs['status'])
        # self.window.m_textCtrl81.SetBackgroundColour(wx.Colour(0, 255, 0))
        # self.window.m_textCtrl6.SetValue('CP Heartbeat')
        return call_result.DiagnosticsStatusNotificationPayload()

    @on(Action.ReserveNow)
    async def Send_ReserveNow(self, re_id):
        self.window.LogMessage2('Send [ReserveNow]')
        self.window.m_textCtrl17.SetValue(datetime.strftime(
            datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"))
        request = call.ReserveNowPayload(connector_id=int(self.window.m_comboBox6.Value), expiry_date=datetime.strftime(
            datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"), id_tag=self.window.m_comboBox5.Value,
            reservation_id=int(re_id), parent_id_tag='str')
        response = await self.call(request)
        if response == None:
            pass
        else:
            self.window.LogMessage1(
                'Receive [ReserveNow status]' + response.status)

    @on(Action.TriggerMessage)
    async def Send_TriggerMessage(self, message_data):
        self.window.LogMessage2('Send [TriggerMessage]')
        if self.window.m_comboBox13.Value == 'BootNotification':
            message_data = MessageTrigger.bootNotification
        elif self.window.m_comboBox13.Value == "MeterValues":
            message_data = MessageTrigger.meterValues
        elif self.window.m_comboBox13.Value == "Heartbeat":
            message_data = MessageTrigger.heartbeat
        elif self.window.m_comboBox13.Value == "StatusNotification":
            message_data = MessageTrigger.statusNotification
        elif self.window.m_comboBox13.Value == "DiagnosticsStatusNotification":
            message_data = MessageTrigger.diagnosticsStatusNotification
        elif self.window.m_comboBox13.Value == "FirmwareStatusNotification":
            message_data = MessageTrigger.firmwareStatusNotification
        request = call.TriggerMessagePayload(
            requested_message=message_data, connector_id=int(self.window.m_comboBox16.Value))
        response = await self.call(request)
        self.window.LogMessage1('Receive [TriggerMessage]' + response.status)

    @on(Action.SetChargingProfile)
    async def Send_SetChargingProfile(self):
        self.window.LogMessage2('Send [SetChargingProfile]')
        smart_profile = {}
        charging_Schedule_Period = [{"startPeriod": 0, "limit": 6.0}, {
            "startPeriod": 60, "limit": 10.0}, {"startPeriod": 120, "limit": 8.0}]
        charging_Schedule = {
            "duration": 300, "startSchedule": "2024-01-17T16:33:16Z", "chargingRateUnit": "A", "chargingSchedulePeriod": charging_Schedule_Period}
        smart_profile = {"chargingProfileId": 2, "stackLevel": 0, "chargingProfilePurpose": "TxDefaultProfile", "chargingProfileKind": "Absolute",
                         "validFrom": "2024-01-17T16:33:16Z", "validTo": "2023-06-19T17:10:00Z", "chargingSchedule": charging_Schedule}
        smart_profile3 = {"chargingProfileId": 2, "stackLevel": 0, "chargingProfilePurpose": "TxDefaultProfile", "chargingProfileKind": "Absolute",
                          "validFrom": "2024-01-17T16:33:16Z", "validTo": "2023-06-19T17:10:00Z", "chargingSchedule":  {
                              "duration": 300, "startSchedule": "2024-01-17T16:33:16Z", "chargingRateUnit": "A", "chargingSchedulePeriod": [{"startPeriod": 0, "limit": 6.0}, {
                                  "startPeriod": 60, "limit": 10.0}, {"startPeriod": 120, "limit": 8.0}]}}
        smart_profile1 = {'csChargingProfiles': {
            'chargingProfileId': 1,
            'stackLevel': 0,
            'chargingProfilePurpose': 'TxProfile',
            'chargingProfileKind': 'Relative',
            'chargingSchedule': {
                'chargingRateUnit': 'A',
                'chargingSchedulePeriod': [{
                    'startPeriod': 0,
                    'limit': 21.4
                }]
            },
            'transactionId': 123456789
        }}
        print(is_dataclass(smart_profile1))
        smart_profile2 = {
            'chargingProfileId': 1,
            'stackLevel': 0,
            'chargingProfilePurpose': 'TxProfile',
            'chargingProfileKind': 'Relative',
            'chargingSchedule': {
                'chargingRateUnit': 'A',
                'chargingSchedulePeriod': [{
                    'startPeriod': 0,
                    'limit': 21.4
                }]
            },
            'transactionId': 123456789
        }
        if self.window.m_comboBox14.Value == "CS_Profile_1":
            CS_Profile = smart_profile3
        else:
            CS_Profile = smart_profile2
        request = call.SetChargingProfilePayload(
            connector_id=1, cs_charging_profiles=CS_Profile)
        response = await self.call(request)
        self.window.LogMessage2('Send finish')
        if request == None:
            pass
        else:
            self.window.LogMessage1(
                'Receive [SetChargingProfile]' + response.status)

    @on(Action.GetCompositeSchedule)
    async def Send_GetCompositeSchedule(self, conn_id, Duration):
        '''"GetCompositeSchedule",{  "connectorId": 1,  "duration": 300}}]'''
        self.window.LogMessage2('Send [GetCompositeSchedule]')
        if self.window.m_comboBox131.Value == 'watts':
            Charg_Type = ChargingRateUnitType.watts
        else:
            Charg_Type = ChargingRateUnitType.amps
        request = call.GetCompositeSchedulePayload(
            connector_id=conn_id, duration=Duration, charging_rate_unit=Charg_Type)
        response = await self.call(request)
        if request == None:
            pass
        else:
            self.window.LogMessage1(
                'Receive [GetCompositeSchedule]' + response.status)

    @on(Action.ClearChargingProfile)
    async def Send_ClearChargingProfile(self):
        self.window.LogMessage2('Send [ClearChargingProfile]')
        request = call.ClearChargingProfilePayload()
        response = await self.call(request)
        self.window.LogMessage1(
            'Receive [ClearChargingProfile]' + response.status)

    @on(Action.DataTransfer)
    async def on_DataTransfer(self, **kwargs):
        self.window.m_textCtrl6.SetValue('DataTransfer')
        self.window.LogMessage1('Receive:DataTransfer')
        self.window.LogMessage1('Vendor_id:'+str(kwargs['vendor_id']))
        self.window.LogMessage1('Message_id'+str(kwargs['message_id']))
        self.window.LogMessage1('Data'+str(kwargs['data']))
        if kwargs['vendor_id'] == self.window.m_textCtrl91.Value:
            return call_result.DataTransferPayload(status='Accepted')
        else:
            return call_result.DataTransferPayload(status='Rejected')

    async def Send_DataTransfer(self):
        self.window.LogMessage2('Send [DataTransfer]')
        request = call.DataTransferPayload(self.window.m_textCtrl91.Value,
                                           self.window.m_textCtrl16.Value, data=self.window.m_textCtrl14.Value)
        response = await self.call(request)
        if response == None:
            pass
        else:
            self.window.LogMessage1(
                'Receive [DataTransfer status]' + response.status)

    @on(Action.RemoteStartTransaction)
    async def Send_RemoteStartTransaction(self, RFID):
        print("on_RemoteStartTransaction.")
        self.window.LogMessage2('Send [RemoteStartTransaction]')
        request = call.RemoteStartTransactionPayload(
            connector_id=1, id_tag=RFID)  # "04B0267AE05C87")
        response = await self.call(request)
        self.window.LogMessage1(
            'Receive [RemoteStartTransaction]' + response.status)
        # return call_result.RemoteStartTransactionPayload(status=RemoteStartStopStatus.accepted)

    @on(Action.RemoteStopTransaction)
    async def Send_RemoteStopTransaction(self, T_id):
        print("on_RemoteStartTransaction.")
        self.window.LogMessage2('Send [RemoteStopTransaction]')
        request = call.RemoteStopTransactionPayload(
            int(T_id))  # "04B0267AE05C87")
        response = await self.call(request)
        self.window.LogMessage1(
            'Receive [RemoteStopTransaction]' + response.status)

    @on(Action.ClearCache)
    async def Send_ClearCache(self, **kwargs):
        print("TC_on_ClearCache.")
        self.window.LogMessage2(u'Send[Clear]')
        request = call.ClearCachePayload()
        response = await self.call(request)

    @on(Action.Reset)
    async def Send_Reset(self, Reset_type):
        print("TC_on_Reset.")
        self.window.LogMessage2(u'Send[Reset]:'+Reset_type)
        if Reset_type == 'Hard':
            R_type = ResetType.hard
        else:
            R_type = ResetType.soft
        request = call.ResetPayload(type=R_type)
        response = await self.call(request)
        self.window.LogMessage1('Receive [Reset]' + response)

    @on(Action.UnlockConnector)
    async def Send_UnlockConnector(self, CP_C_id):
        print("TC_on_UnlockConnector.")
        self.window.LogMessage2(u'Send[UnlockConnector]')
        request = call.UnlockConnectorPayload(connector_id=CP_C_id)
        response = await self.call(request)
        self.window.LogMessage1('Receive [UnlockConnector]' + response.status)

    @on(Action.GetLog)
    async def on_GetLog(self, **kwargs):
        print("TC_on_GetLog.")
        # for 079
        return call_result.GetLogPayload(status=LogStatus.accepted, filename='CP_log')

    @after(Action.GetLog)
    async def Send_LogStatusNotification(self, **kwargs):
        # for 079
        await asyncio.sleep(5)
        self.window.LogMessage2(
            u'"LogStatusNotification: Uploading' + '\r\n')
        request = call.LogStatusNotificationPayload(
            request_id=1, status=UploadLogStatus.uploading)
        response = await self.call(request)
        print("LogStatusNotification_Uploaded")
        await asyncio.sleep(5)
        self.window.LogMessage2(
            u'"LogStatusNotification: Uploading' + '\r\n')
        request = call.LogStatusNotificationPayload(
            request_id=1, status=UploadLogStatus.uploaded)
        response = await self.call(request)
        print("LogStatusNotification_Uploaded")
        # self.window.m_textCtrl6.SetBackgroundColour(wx.Colour(0, 255, 0))
        # self.window.m_textCtrl6.SetValue('Preparing')

    @on(Action.ExtendedTriggerMessage)
    async def on_ExtendedTriggerMessage(self, **kwargs):
        print("TC_on_ExtendedTriggerMessage.")
        # for 074
        return call_result.ExtendedTriggerMessagePayload(status=TriggerMessageStatus.accepted)

    @after(Action.ExtendedTriggerMessage)
    async def Send_SignCertificate(self, **kwargs):
        # for 074
        await asyncio.sleep(5)
        self.window.LogMessage2(
            u'SignCertificate: Uploading' + '\r\n')
        request = call.SignCertificatePayload(csr="-----BEGIN NEW CERTIFICATE REQUEST-----\r\nMIICpjCCAY4CAQAwYTELMAkGA1UEBhMCSU4xFTATBgNVBAgTDFV0dGFyUHJhZGVz\r\naDEOMAwGA1UEBxMFTm9pZGExDDAKBgNVBAoTA09DQTELMAkGA1UECxMCSVQxEDAO\r\nBgNVBAMTB09DQVRFU1QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC5\r\nEUy9QdkVc8Hk3uvEDrXTgFi6wZWjHrjDLHgEQR9/NFdLjhs6IUGwyqBcDFdAHBZv\r\n8j+BRSkVHhEQPDnguWCx1/T9zlNIj02+ctDABYz7gXuRCzQOOCn1ONclFpnk2wAP\r\nW1jw1qLJENnXtvEkMdnygR3dx7MXKsFvRXn73K1QueThhO46YsQRe6NHBk9bfF6Y\r\nkQYYMkfsthvFXsRQtbmnJjgS8TbZKs2ZSsunHtVFJNiyvinRQDIoaHa4v5wmy0tK\r\nLaAL7Y9Ahdep8/vhLn/4q1XABuMQ6Fbwd2L0s158YqoDk0b7lTPrwRSiHT0SEOmM\r\nL02MdUpnJwOL6JqXKdgjAgMBAAGgADANBgkqhkiG9w0BAQUFAAOCAQEAoVll81fB\r\n96uaZR/UgZ1831iiKodQtL8ixdUqhseSyqD7SwUvN9W9lQg6fBThuFtC1sna3k1O\r\nbvMCFdnRo6bx2b9f5lzxT+ppmB+274IOLUJixY+HGXQ2yTkkGNQYrvnM8+HKcw7e\r\nyy0h47IPzKkYXDZTCvGO9n5POYSWmTDtrujtMWwoKUP9aNC05706TGILHtMtfr6g\r\nL07grn4I33hGj0OAu/tyRP4srrecm9rs7upXCjh56RU7Vg9EhoQRQpsa948Nh3vO\r\n9dNodj5pdcvSMKnsnwi8kzymi6pTvqpobjFLv4zoDoNPAHUyDqJH9owVrJ6aVQ/5\r\nOqGNMi/VNc7GrA==\r\n-----END NEW CERTIFICATE REQUEST-----\r\n")
        response = await self.call(request)
        print("SignCertificatePayload_send")

    @on(Action.CertificateSigned)
    async def on_CertificateSignedMessage(self, **kwargs):
        print("TC_on_CertificateSignedMessage.")
        # for 074&77
        if self.window.m_comboBox8.Value == 'Invalid_CA':
            return call_result.CertificateSignedPayload(status=CertificateSignedStatus.rejected)
        else:
            return call_result.CertificateSignedPayload(status=CertificateSignedStatus.rejected)

    @after(Action.CertificateSigned)
    async def Send_CP_UpdateCA(self, **kwargs):
        # for 074
        await asyncio.sleep(5)
        if self.window.m_comboBox8.Value == 'Valid_CA':
            self.window.LogMessage2(u'CP_CA_Update' + '\r\n')
            # global ws
            # 斷線重新用新CA連線
            await self.ws.close()
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            # ssl_context.load_default_certs()
            path_cert = pathlib.Path(__file__).with_name('RootCA_RSA.pem')
            path_key = pathlib.Path(__file__).with_name('RootCA_RSA_Key.pem')
            ssl_context.load_cert_chain(path_cert, keyfile=path_key)
            print('test')
            # async with websockets.connect("wss://OCATEST:OCATEST@192.168.14.30:9001/ocpp/", ssl=ssl_context, subprotocols=['ocpp1.6']) as ws:
            async with websockets.connect(self.m_textCtrl3.Value, ssl=ssl_context, subprotocols=['ocpp1.6']) as self.ws:
                self.LogMessage2(self.m_textCtrl3.Value+'_Profile_3')
        else:
            request = call.SecurityEventNotificationPayload(type='InvalidChargePointCertificate', timestamp=datetime.strftime(
                datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"), tech_info='rsa')
            response = await self.call(request)

    @on(Action.InstallCertificate)
    async def on_InstallCertificate(self, **kwargs):
        print("TC_on_InstallCertificate.")
        # for 075
        global delet_ca
        delet_ca = 0
        # kwargs['certificate']==1:
        if self.window.m_comboBox7.Value == 'Invalid_CA':
            return call_result.InstallCertificatePayload(status=CertificateStatus.rejected)
        else:
            return call_result.InstallCertificatePayload(status=CertificateStatus.accepted)

    @after(Action.InstallCertificate)
    async def Send_SecurityEventNotification(self, **kwargs):
        await asyncio.sleep(5)
        self.window.LogMessage2(u'SecurityEventNotification' + '\r\n')
        if self.window.m_comboBox7.Value == 'Invalid_CA':
            request = call.SecurityEventNotificationPayload(type='InvalidCentralSystemCertificate', timestamp=datetime.strftime(
                datetime.utcnow(), "%Y-%m-%dT%H:%M:%SZ"), tech_info='rsa')
            response = await self.call(request)
        print("SecurityEventNotification_send")

    @on(Action.GetInstalledCertificateIds)
    async def on_GetInstalledCertificateIds(self, **kwargs):
        print("TC_on_GetInstalledCertificateIds.")
        # for 075&076
        if delet_ca == 0:
            payload = [{"hashAlgorithm": "SHA256", "issuerNameHash": "e60bd843bf2279339127ca19ab6967081dd6f95e745dc8b8632fa56031debe5b",
                        "issuerKeyHash": "cb6f81a01813e47d84b03fe1b12de1ecc3c0f543532f5c559395635f169e25f9", "serialNumber": "3"}]
        else:
            payload = [{"hashAlgorithm": "SHA256", "issuerNameHash": "aaabd843bf2279339127ca19ab6967081dd6f95e745dc8b8632fa56031debe5b",
                        "issuerKeyHash": "aaaf81a01813e47d84b03fe1b12de1ecc3c0f543532f5c559395635f169e25f9", "serialNumber": "4"}]
        return call_result.GetInstalledCertificateIdsPayload(status=GetInstalledCertificateStatus.accepted, certificate_hash_data=payload)

    @on(Action.DeleteCertificate)
    async def on_DeleteCertificate(self, **kwargs):
        print("TC_on_DeleteCertificate.")
        # for 076
        global delet_ca
        delet_ca = 1
        return call_result.DeleteCertificatePayload(status=DeleteCertificateStatus.accepted)


class OCPP16J_Main1(OCPP_CS_GUIv4_2024.MyFrame2):
    def __init__(self, parent):
        OCPP_CS_GUIv4_2024.MyFrame2.__init__(self, parent)
        self.m_comboBox1.Append('Charging Point')
        self.m_comboBox1.Append('Cental System')
        self.m_comboBox5.Append('04B0267AE05C87')
        self.m_comboBox5.Append('expired')
        self.m_comboBox5.Append('blocked')
        wxasync.AsyncBind(wx.EVT_BUTTON, self.OCPP_Link, self.m_button101)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.OCPP_Disconnect, self.m_button10)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.UnlockConnector, self.m_button111)
        # wxasync.AsyncBind(wx.EVT_BUTTON, self.Check_ID, self.m_button151)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.CancelReservation, self.m_button8)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.ChangeConfiguration, self.m_button17)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.ChangeAvailability, self.m_button18)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.Get_Local_List, self.m_button28)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.FirmwareUpdate, self.m_button181)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.P1_link, self.m_button20)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.P2_link, self.m_button21)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.P3_link, self.m_button22)
        # wxasync.AsyncBind(wx.EVT_BUTTON, self.Clear_Rlog, self.m_button171)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.RStart_Charging, self.m_button15)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.RStop_Charging, self.m_button16)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.ClearCache, self.m_button19)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.Reset, self.m_button9)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.GetConfiguration, self.m_button26)

        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.Send_Local_Authorization, self.m_button221)

        # firmware.location is <Firmware Download URL from test data>
        wxasync.AsyncBind(wx.EVT_BUTTON, self.GetDiagnostics, self.m_button27)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.ReserveNow, self.m_button13)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.TriggerMessage, self.m_button12)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.SetChargingProfile, self.m_button14)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.GetCompositeSchedule, self.m_button25)
        wxasync.AsyncBind(
            wx.EVT_BUTTON, self.ClearChargingProfile, self.m_button23)
        wxasync.AsyncBind(wx.EVT_BUTTON, self.DataTransfer, self.m_button24)

        global OCPP_Status
        global CS_Status
        OCPP_Status = 0  # 0_nolink, 1_Link
        CS_Status = 0  # 0_idle, 1_Availble, 2_Prepairing, 3_Charging, 4_SuspendedEV, 5_SuspendedEVSE, 6_Finishing, 7_Reserved, 8_Unavailable, 9_Faulted

        # ----------------Com port---------------------

    def LogMessage1(self, msg):
        self.m_textCtrl5.SetInsertionPoint(0)
        self.m_textCtrl5.WriteText(msg+'\r\n')

    def LogMessage2(self, msg):
        self.m_textCtrl8.SetInsertionPoint(0)
        self.m_textCtrl8.WriteText(msg+'\r\n')

    def Clear_Slog(self, event):
        self.m_textCtrl8.SetInsertionPoint(0)
        self.m_textCtrl8.SetValue("")

    def Clear_Rlog(self, event):
        self.m_textCtrl5.SetInsertionPoint(0)
        self.m_textCtrl5.SetValue("")

    def T_Finsh(self):
        self.m_button4.Enable(1)
        self.m_button5.Enable(0)
        # self.ton1_Switch(0,'0')
        if self.m_checkBox7.Value:
            self.Packet_Analyzer(self.m_comboBox4.GetSelection(
            ), Save_Path+'\\'+str(self.m_comboBox4.Value)+'.pcap')
            # wx.MessageBox(str(self.m_comboBox4.GetSelection()))

    async def OCPP_Disconnect(self, event):
        global server
        server.wait_closed()
        self.LogMessage2(u'server 中斷連線'+'\r\n')

    async def CancelReservation(self, event):
        # TODO: CancelReservation
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_CancelReservation(int(self.m_textCtrl15.Value))

    async def ChangeConfiguration(self, event):
        # TODO: ChangeConfiguration
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_ChangeConfiguration(self.m_comboBox10.Value, self.m_comboBox15.Value)

    async def ChangeAvailability(self, event):
        # TODO: ChangeAvailability
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_ChangeAvailability(int(self.m_comboBox17.Value))

    async def FirmwareUpdate(self, event):
        # TODO: FirmwareUpdate
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_FirmwareUpdate(self.m_comboBox12.Value)
        # firmware.location is <Firmware Download URL from test data>

    async def Get_Local_List(self, event):
        # TODO: FirmwareUpdate
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_Get_Local_List()

    async def Send_Local_Authorization(self, event):
        # TODO: Send_Local_Authorization
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_Local_Authorization(self.m_comboBox111.Value)

    async def GetConfiguration(self, event):
        # TODO: RStop_Charging
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_GetConfiguration(self.m_comboBox10.Value)

    async def GetDiagnostics(self, event):
        # TODO: GetDiagnostics
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_GetDiagnostics()

    async def ReserveNow(self, event):
        # TODO: ReserveNow
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_ReserveNow(self.m_textCtrl15.Value)

    async def TriggerMessage(self, event):
        # TODO: TriggerMessage
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_TriggerMessage(self.m_comboBox13.Value)

    async def SetChargingProfile(self, event):
        # TODO: SetChargingProfile
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_SetChargingProfile()

    async def GetCompositeSchedule(self, event):
        # TODO: GetCompositeSchedule
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_GetCompositeSchedule(int(self.m_comboBox18.Value), int(self.m_textCtrl18.Value))

    async def ClearChargingProfile(self, event):
        # TODO: ClearChargingProfile
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_ClearChargingProfile()

    async def DataTransfer(self, event):
        # TODO: DataTransfer
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_DataTransfer()

    async def Start_Charging(self, event):
        # TODO: Start_Charging
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        if self.m_button111.LabelText == u'開始充電':
            await cp1.send_StartTransactionPayload()
            self.m_button111.SetLabel(u'充電中')
        else:
            await cp1.send_StopTransactionPayload()
            self.m_button111.SetLabel(u'開始充電')

    async def ClearCache(self, event):
        # TODO: ClearCache
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_ClearCache()

    async def Reset(self, event):
        # TODO: ClearCache
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_Reset(self.m_comboBox11.Value)

    async def RStart_Charging(self, event):
        # TODO: RStart_Charging
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        if self.m_button15.LabelText == u'遠端開始充電':
            self.m_button15.SetLabel(u'充電中')
            await cp1.Send_RemoteStartTransaction(self.m_comboBox5.Value)

        else:
            # await cp1.Send_RemoteStartTransaction(self.m_comboBox5.Value)
            self.m_button15.SetLabel(u'遠端開始充電')

    async def UnlockConnector(self, event):
        # TODO: RStop_Charging
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        await cp1.Send_UnlockConnector(int(self.m_comboBox16.Value))

    async def RStop_Charging(self, event):
        # TODO: RStop_Charging
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global cp1
        self.m_button15.SetLabel(u'遠端開始充電')
        await cp1.Send_RemoteStopTransaction(int(self.m_textCtrl10.Value))

    async def on_connect(self, websocket, path):
        """ For every new charge point that connects, create a ChargePoint
        instance and start listening for messages.
        """
        global cp1
        global OCPP_Status
        global CS_Status
        try:
            requested_protocols = websocket.request_headers[
                'Sec-WebSocket-Protocol']
        except KeyError:
            logging.error(
                "Client hasn't requested any Subprotocol. Closing Connection"
            )
            return await websocket.close()
        if websocket.subprotocol:
            logging.info("Protocols Matched: %s", websocket.subprotocol)
        else:
            # In the websockets lib if no subprotocols are supported by the
            # client and the server, it proceeds without a subprotocol,
            # so we have to manually close the connection.
            logging.warning('Protocols Mismatched | Expected Subprotocols: %s,'
                            ' but client supports  %s | Closing connection',
                            websocket.available_subprotocols,
                            requested_protocols)
            return await websocket.close()

        charge_point_id = path.strip('/')
        cp1 = ChargePoint(charge_point_id, websocket, self)
        self.LogMessage2('OCPP Server Oonnect')
        self.m_textCtrl81.SetValue('OCPP CP Oonnect')
        # OCPP_Status = 1
        # CS_Status = 1
        await cp1.start()

    async def OCPP_Link(self, event):
        # TODO: Implement Start
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        global server
        try:
            if self.m_comboBox2.Value == "Profile_0":
                # str(self.m_textCtrl3.Value)  # "192.168.14.26"
                # str(self.m_textCtrl3.Value)  # '0.0.0.0'
                ws_url = str(self.m_textCtrl3.Value)  # "192.168.14.26"
                ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
                subprotocols = ['ocpp1.6']
                idTag_client = "00000000"
                connectorId_client = None
                transactionId_client = None

                fgRxAuthorize = False
                fgRxStartTransaction = False
                fgRxStopTransaction = False

                server = await websockets.serve(ws_handler=self.on_connect,
                                                host=ws_url,
                                                port=ws_port,
                                                subprotocols=subprotocols)
            # , cp.send_boot_notification())
            elif self.m_comboBox2.Value == "Profile_1":
                UserName = str(self.m_textCtrl3.Value)[:
                                                       str(self.m_textCtrl3.Value).find(':')]  # 'OCATEST'
                PassWord = str(self.m_textCtrl3.Value)[
                    str(self.m_textCtrl3.Value).find(':')+1:str(self.m_textCtrl3.Value).find('@')]  # 'OCATEST'
                ws_url = str(self.m_textCtrl3.Value)[
                    str(self.m_textCtrl3.Value).find('@')+1:]  # '0.0.0.0'
                ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
                subprotocols = ['ocpp1.6']
                idTag_client = "00000000"
                connectorId_client = None
                transactionId_client = None

                fgRxAuthorize = False
                fgRxStartTransaction = False
                fgRxStopTransaction = False
                basic_auth = websockets.basic_auth_protocol_factory(
                    realm='example', credentials=(UserName, PassWord))
                server = await websockets.serve(ws_handler=self.on_connect,
                                                host=ws_url,
                                                port=ws_port,
                                                create_protocol=basic_auth,
                                                subprotocols=subprotocols)
            elif self.m_comboBox2.Value == "Profile_2":
                ChargePoint_CA_Path = './certs/CP_RSA.pem'
                CentralSystem_CA_Path = './certs/CSMS_RSA.pem'
                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                # ssl_context.load_default_certs()
                path_cert = pathlib.Path(__file__).with_name('CP_RSA.pem')
                path_key = pathlib.Path(__file__).with_name('CP_RSA_Key.pem')
                ssl_context.load_cert_chain(path_cert, keyfile=path_key)
                print('test')
                UserName = str(self.m_textCtrl3.Value)[:
                                                       str(self.m_textCtrl3.Value).find(':')]  # 'OCATEST'
                PassWord = str(self.m_textCtrl3.Value)[
                    str(self.m_textCtrl3.Value).find(':')+1:str(self.m_textCtrl3.Value).find('@')]  # 'OCATEST'
                basic_auth = websockets.basic_auth_protocol_factory(
                    realm='example', credentials=(UserName, PassWord))

                ws_url = str(self.m_textCtrl3.Value)[
                    str(self.m_textCtrl3.Value).find('@')+1:]  # '0.0.0.0'
                ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
                subprotocols = ['ocpp1.6']
                idTag_client = "00000000"
                connectorId_client = None
                transactionId_client = None

                fgRxAuthorize = False
                fgRxStartTransaction = False
                fgRxStopTransaction = False

                server = await websockets.serve(ws_handler=self.on_connect,
                                                host=ws_url,
                                                port=ws_port,
                                                create_protocol=basic_auth,
                                                ssl=ssl_context,
                                                subprotocols=subprotocols)
            elif self.m_comboBox2.Value == "Profile_3":
                ChargePoint_CA_Path = './certs/CP_RSA.pem'
                CentralSystem_CA_Path = './certs/CSMS_RSA.pem'
                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                # ssl_context.load_default_certs()
                path_cert = pathlib.Path(__file__).with_name('CP_RSA.pem')
                path_key = pathlib.Path(__file__).with_name('CP_RSA_Key.pem')
                ssl_context.load_cert_chain(path_cert, keyfile=path_key)
                print('test')
                ws_url = str(self.m_textCtrl3.Value)  # '0.0.0.0'
                ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
                subprotocols = ['ocpp1.6']
                idTag_client = "00000000"
                connectorId_client = None
                transactionId_client = None

                fgRxAuthorize = False
                fgRxStartTransaction = False
                fgRxStopTransaction = False

                server = await websockets.serve(ws_handler=self.on_connect,
                                                host=ws_url,
                                                port=ws_port,
                                                ssl=ssl_context,
                                                subprotocols=subprotocols)
            self.LogMessage2('OCPP Server IP: '+ws_url+'\r\n')
            self.LogMessage2('OCPP Server port: '+str(ws_port)+'\r\n')
            self.LogMessage2('OCPP Server Version: '+str(subprotocols)+'\r\n')
            self.LogMessage2('OCPP Server Security Level: ' +
                             self.m_comboBox2.Value)

            self.m_textCtrl81.SetValue('Server On at:'+self.m_comboBox2.Value)
            # self.m_textCtrl6.SetBackgroundColour(wx.Colour(255, 255, 255))
        except:
            self.LogMessage1(u'OCPP error message: ' + str('e')+'\r\n')
            await server.wait_closed()
            # exit()
        # --------------------------------------------------------------------
        pass

    def Change_Sec(self, event):
        if '@' in str(self.m_textCtrl3.Value):
            print(str(self.m_textCtrl3.Value).find('@'))
            url = str(self.m_textCtrl3.Value)[
                str(self.m_textCtrl3.Value).find('@')+1:]
        else:
            url = str(self.m_textCtrl3.Value)
        if self.m_comboBox2.Value == 'Profile_1':
            self.m_textCtrl3.SetValue("OCATEST:OCATEST@"+url)
        elif self.m_comboBox2.Value == 'Profile_2':
            self.m_textCtrl3.SetValue("OCATEST:OCATEST@"+url)
        elif self.m_comboBox2.Value == 'Profile_3':
            self.m_textCtrl3.SetValue(url)
        else:
            self.m_textCtrl3.SetValue(url)

    async def P1_link(self, event):
        # TODO: Implement Start
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        try:
            UserName = str(self.m_textCtrl3.Value)[:
                                                   str(self.m_textCtrl3.Value).find(':')]  # 'OCATEST'
            PassWord = str(self.m_textCtrl3.Value)[
                str(self.m_textCtrl3.Value).find(':')+1:str(self.m_textCtrl3.Value).find('@')]  # 'OCATEST'
            ws_url = str(self.m_textCtrl3.Value)[
                str(self.m_textCtrl3.Value).find('@')+1:]  # '0.0.0.0'
            ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
            subprotocols = ['ocpp1.6']
            idTag_client = "00000000"
            connectorId_client = None
            transactionId_client = None

            fgRxAuthorize = False
            fgRxStartTransaction = False
            fgRxStopTransaction = False
            basic_auth = websockets.basic_auth_protocol_factory(
                realm='example', credentials=(UserName, PassWord))
            server = await websockets.serve(ws_handler=self.on_connect,
                                            host=ws_url,
                                            port=ws_port,
                                            create_protocol=basic_auth,
                                            subprotocols=subprotocols)
            self.LogMessage2(self.m_textCtrl3.Value+'_Profile_1')
            self.LogMessage2('OCPP Server IP: '+ws_url+'\r\n')
            self.LogMessage2('OCPP Server port: '+str(ws_port)+'\r\n')
            self.LogMessage2('OCPP Server Version: '+str(subprotocols)+'\r\n')
            # , cp.send_boot_notification())
            self.m_textCtrl81.SetValue('Server On')
            # self.m_textCtrl6.SetBackgroundColour(wx.Colour(255, 255, 255))
        except:
            self.LogMessage1(u'OCPP error message: ' + str('e')+'\r\n')
            await server.wait_closed()
            # exit()
        # --------------------------------------------------------------------
        pass

    async def P2_link(self, event):
        # TODO: Implement Start
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        try:
            ChargePoint_CA_Path = './certs/CP_RSA.pem'
            CentralSystem_CA_Path = './certs/CSMS_RSA.pem'
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            # ssl_context.load_default_certs()
            path_cert = pathlib.Path(__file__).with_name('CP_RSA.pem')
            path_key = pathlib.Path(__file__).with_name('CP_RSA_Key.pem')
            ssl_context.load_cert_chain(path_cert, keyfile=path_key)
            print('test')
            UserName = str(self.m_textCtrl3.Value)[:
                                                   str(self.m_textCtrl3.Value).find(':')]  # 'OCATEST'
            PassWord = str(self.m_textCtrl3.Value)[
                str(self.m_textCtrl3.Value).find(':')+1:str(self.m_textCtrl3.Value).find('@')]  # 'OCATEST'
            basic_auth = websockets.basic_auth_protocol_factory(
                realm='example', credentials=(UserName, PassWord))

            ws_url = str(self.m_textCtrl3.Value)[
                str(self.m_textCtrl3.Value).find('@')+1:]  # '0.0.0.0'
            ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
            subprotocols = ['ocpp1.6']
            idTag_client = "00000000"
            connectorId_client = None
            transactionId_client = None

            fgRxAuthorize = False
            fgRxStartTransaction = False
            fgRxStopTransaction = False

            server = await websockets.serve(ws_handler=self.on_connect,
                                            host=ws_url,
                                            port=ws_port,
                                            create_protocol=basic_auth,
                                            ssl=ssl_context,
                                            subprotocols=subprotocols)
            self.LogMessage2(self.m_textCtrl3.Value+'_Profile_2')
            self.LogMessage2('OCPP Server IP: '+ws_url+'\r\n')
            self.LogMessage2('OCPP Server port: '+str(ws_port)+'\r\n')
            self.LogMessage2('OCPP Server Version: '+str(subprotocols)+'\r\n')
            # , cp.send_boot_notification())
            self.m_textCtrl81.SetValue('Server On')
            # self.m_textCtrl6.SetBackgroundColour(wx.Colour(255, 255, 255))
        except:
            self.LogMessage1(u'OCPP error message: ' + str('e')+'\r\n')
            await server.wait_closed()
            # exit()
        # --------------------------------------------------------------------
        pass

    async def P3_link(self, event):
        # TODO: Implement Start
        # ----------------------------------------------------------------------
        # --------------------------------------------------------------------
        try:
            ChargePoint_CA_Path = './certs/CP_RSA.pem'
            CentralSystem_CA_Path = './certs/CSMS_RSA.pem'
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            # ssl_context.load_default_certs()
            path_cert = pathlib.Path(__file__).with_name('CP_RSA.pem')
            path_key = pathlib.Path(__file__).with_name('CP_RSA_Key.pem')
            ssl_context.load_cert_chain(path_cert, keyfile=path_key)
            print('test')
            ws_url = str(self.m_textCtrl3.Value)  # '0.0.0.0'
            ws_port = int(self.m_textCtrl121.Value)  # 9001 /9000
            subprotocols = ['ocpp1.6']
            idTag_client = "00000000"
            connectorId_client = None
            transactionId_client = None

            fgRxAuthorize = False
            fgRxStartTransaction = False
            fgRxStopTransaction = False

            server = await websockets.serve(ws_handler=self.on_connect,
                                            host=ws_url,
                                            port=ws_port,
                                            ssl=ssl_context,
                                            subprotocols=subprotocols)
            self.LogMessage2(self.m_textCtrl3.Value+'_Profile_3')
            self.LogMessage2('OCPP Server IP: '+ws_url+'\r\n')
            self.LogMessage2('OCPP Server port: '+str(ws_port)+'\r\n')
            self.LogMessage2('OCPP Server Version: '+str(subprotocols)+'\r\n')
            # , cp.send_boot_notification())
            self.m_textCtrl81.SetValue('Server On')
            # self.m_textCtrl6.SetBackgroundColour(wx.Colour(255, 255, 255))
        except:
            self.LogMessage1(u'OCPP error message: ' + str('e')+'\r\n')
            await server.wait_closed()
            # exit()
        # --------------------------------------------------------------------
        pass


'''ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.check_hostname = True
ctx.load_verify_locations('certificates/server_cert.pem')
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_cert_chain('certificates/bob_cert.pem', 'certificates/bob_key.pem')'''

if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wxasync.WxAsyncApp()
    frm = OCPP16J_Main1(None)
    frm.Show()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.MainLoop())
