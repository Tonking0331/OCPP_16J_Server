# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ETCCP (OCPP_CS)", pos = wx.DefaultPosition, size = wx.Size( 851,547 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"OCPP裝置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer7.Add( self.m_staticText1, 0, wx.ALL, 5 )

		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Central System", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer7.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"加密類別", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )

		m_comboBox2Choices = [ u"Profile_0", u"Profile_1", u"Profile_2", u"Profile_3", u"Profile_4" ]
		self.m_comboBox2 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Profile_0", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		bSizer7.Add( self.m_comboBox2, 0, wx.ALL, 5 )

		self.m_button111 = wx.Button( self.m_panel2, wx.ID_ANY, u"解鎖連接器", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button111, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		m_comboBox16Choices = [ u"1", u"2" ]
		self.m_comboBox16 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox16Choices, 0 )
		bSizer7.Add( self.m_comboBox16, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"時區", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		bSizer7.Add( self.m_staticText48, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		m_comboBox19Choices = [ u"System", u"UTC" ]
		self.m_comboBox19 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"System", wx.DefaultPosition, wx.DefaultSize, m_comboBox19Choices, 0 )
		bSizer7.Add( self.m_comboBox19, 1, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"CS_D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer7.Add( self.m_staticText13, 0, wx.ALL, 5 )

		m_comboBox7Choices = [ u"Valid_CA", u"Invalid_CA" ]
		self.m_comboBox7 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Valid_CA", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		bSizer7.Add( self.m_comboBox7, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText14 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"CP_D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer7.Add( self.m_staticText14, 0, wx.ALL, 5 )

		m_comboBox8Choices = [ u"Valid_CA", u"Invalid_CA" ]
		self.m_comboBox8 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Valid_CA", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, 0 )
		bSizer7.Add( self.m_comboBox8, 0, wx.TOP|wx.BOTTOM, 5 )


		bSizer20.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"CS_IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer8.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"192.168.130.238", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		bSizer8.Add( self.m_staticText141, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		self.m_textCtrl121 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"9001", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl121, 1, wx.TOP|wx.BOTTOM, 5 )

		self.m_button101 = wx.Button( self.m_panel2, wx.ID_ANY, u"OCPP_CS 開啟", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button101, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"廠牌", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer8.Add( self.m_staticText15, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl4, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"型號", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer8.Add( self.m_staticText6, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl91 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl91, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText212 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MsgID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		bSizer8.Add( self.m_staticText212, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl16, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"CS狀態", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer111.Add( self.m_staticText16, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_textCtrl81 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_textCtrl81, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Idtag", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer111.Add( self.m_staticText7, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		m_comboBox5Choices = []
		self.m_comboBox5 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"accepted", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
		bSizer111.Add( self.m_comboBox5, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self.m_panel2, wx.ID_ANY, u"遠端開始充電", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_button15, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button16 = wx.Button( self.m_panel2, wx.ID_ANY, u"遠端停止充電", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_button16, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button9 = wx.Button( self.m_panel2, wx.ID_ANY, u"CP重置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"重置方式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer111.Add( self.m_staticText26, 0, wx.ALL, 5 )

		m_comboBox11Choices = [ u"Hard", u"Soft" ]
		self.m_comboBox11 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Hard", wx.DefaultPosition, wx.DefaultSize, m_comboBox11Choices, 0 )
		bSizer111.Add( self.m_comboBox11, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer111, 1, wx.EXPAND, 5 )

		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText111 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"充電樁狀態", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		bSizer201.Add( self.m_staticText111, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"Idel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_textCtrl6.SetMinSize( wx.Size( 70,-1 ) )

		bSizer201.Add( self.m_textCtrl6, 0, wx.TOP|wx.LEFT, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"交易ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer201.Add( self.m_staticText11, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"1234567", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.m_textCtrl10, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"開始度數", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer201.Add( self.m_staticText21, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl11.SetMinSize( wx.Size( 70,-1 ) )

		bSizer201.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"結束", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer201.Add( self.m_staticText9, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl12.SetMinSize( wx.Size( 70,-1 ) )

		bSizer201.Add( self.m_textCtrl12, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"理由", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer201.Add( self.m_staticText17, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.m_textCtrl13, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button10 = wx.Button( self.m_panel2, wx.ID_ANY, u"OCPP斷線", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.m_button10, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		bSizer20.Add( bSizer201, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button181 = wx.Button( self.m_panel2, wx.ID_ANY, u"更新韌體", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button181, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText43 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer17.Add( self.m_staticText43, 0, wx.ALL, 5 )

		m_comboBox12Choices = [ u"https://www.google.co.in", u"ftp://google.com", u"ftp://OCATEST:OCATEST@192.168.130.238:2121/", wx.EmptyString ]
		self.m_comboBox12 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"https://www.google.co.in", wx.DefaultPosition, wx.DefaultSize, m_comboBox12Choices, 0 )
		self.m_comboBox12.SetMinSize( wx.Size( 50,-1 ) )

		bSizer17.Add( self.m_comboBox12, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_button271 = wx.Button( self.m_panel2, wx.ID_ANY, u"安全韌體更新", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button271, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText47 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Retry時間差(min)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		bSizer17.Add( self.m_staticText47, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl22.SetMinSize( wx.Size( 50,-1 ) )

		bSizer17.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Retry", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_checkBox1, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText45 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"次數", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		bSizer17.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl20.SetMinSize( wx.Size( 50,-1 ) )

		bSizer17.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"間隔", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		bSizer17.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.m_textCtrl211 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl211.SetMinSize( wx.Size( 50,-1 ) )

		bSizer17.Add( self.m_textCtrl211, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText44 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"CA路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer211.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer211.Add( self.m_filePicker1, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		self.m_button24 = wx.Button( self.m_panel2, wx.ID_ANY, u"資料傳輸", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_button24, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText42 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer211.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"ftp://OCATEST:OCATEST@192.168.130.238:2121/", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_textCtrl14, 1, wx.TOP|wx.BOTTOM, 5 )


		bSizer20.Add( bSizer211, 0, wx.EXPAND, 5 )


		bSizer12.Add( bSizer20, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer12 )
		self.m_panel2.Layout()
		bSizer12.Fit( self.m_panel2 )
		bSizer11.Add( self.m_panel2, 0, wx.EXPAND|wx.RIGHT, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel21 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Send Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer13.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_button161 = wx.Button( self.m_panel21, wx.ID_ANY, u"Clear_Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button161, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer13, 0, 0, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer9.Add( self.m_textCtrl8, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText112 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Riceive Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )

		bSizer14.Add( self.m_staticText112, 0, wx.ALL, 5 )

		self.m_button171 = wx.Button( self.m_panel21, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button171, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self.m_panel21, wx.ID_ANY, u"P1_link", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self.m_panel21, wx.ID_ANY, u"P2_link", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button21, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self.m_panel21, wx.ID_ANY, u"P3_link", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button22, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer14, 0, 0, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer10.Add( self.m_textCtrl5, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.m_panel21.SetSizer( bSizer33 )
		self.m_panel21.Layout()
		bSizer33.Fit( self.m_panel21 )
		self.m_notebook1.AddPage( self.m_panel21, u"Send/Riceive Message", True )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button17 = wx.Button( self.m_panel3, wx.ID_ANY, u"變更組態", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button17, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button26 = wx.Button( self.m_panel3, wx.ID_ANY, u"取得組態資訊", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button26, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button19 = wx.Button( self.m_panel3, wx.ID_ANY, u"清除快取", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button19, 0, wx.TOP|wx.BOTTOM, 5 )

		m_comboBox61Choices = [ u"SignatureVerified", u"InvalidSignature" ]
		self.m_comboBox61 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"SignatureVerified", wx.DefaultPosition, wx.DefaultSize, m_comboBox61Choices, 0 )
		bSizer15.Add( self.m_comboBox61, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"-1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl9, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button27 = wx.Button( self.m_panel3, wx.ID_ANY, u"取得診斷資訊", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button27, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText29 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"診斷資訊路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer15.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"ftp://OCATEST:OCATEST@192.168.130.238:2121/", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl21, 1, wx.ALL, 5 )


		bSizer19.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button14 = wx.Button( self.m_panel3, wx.ID_ANY, u"設定充電剖繪", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button14, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button23 = wx.Button( self.m_panel3, wx.ID_ANY, u"清除充電剖繪", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button23, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button25 = wx.Button( self.m_panel3, wx.ID_ANY, u"取得複合排程", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button25, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText28 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"連接器ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer21.Add( self.m_staticText28, 0, wx.ALL, 5 )

		m_comboBox18Choices = [ u"1", u"2" ]
		self.m_comboBox18 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox18Choices, 0 )
		bSizer21.Add( self.m_comboBox18, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer21.Add( self.m_staticText24, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl18.SetMinSize( wx.Size( 50,-1 ) )

		bSizer21.Add( self.m_textCtrl18, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		m_comboBox14Choices = [ u"CS_Profile_1", u"CS_Profile_2" ]
		self.m_comboBox14 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"CS_Profile_1", wx.DefaultPosition, wx.DefaultSize, m_comboBox14Choices, 0 )
		bSizer21.Add( self.m_comboBox14, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ChargingRateUnit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer21.Add( self.m_staticText25, 0, wx.TOP|wx.BOTTOM, 5 )

		m_comboBox131Choices = [ u"watts", u"amps" ]
		self.m_comboBox131 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"watts", wx.DefaultPosition, wx.DefaultSize, m_comboBox131Choices, 0 )
		bSizer21.Add( self.m_comboBox131, 0, wx.ALL, 5 )


		bSizer19.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button18 = wx.Button( self.m_panel3, wx.ID_ANY, u"變更可用性", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button18, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText27 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"連接器ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer16.Add( self.m_staticText27, 0, wx.ALL, 5 )

		m_comboBox17Choices = [ u"1", u"2" ]
		self.m_comboBox17 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox17Choices, 0 )
		bSizer16.Add( self.m_comboBox17, 0, wx.ALL, 5 )

		self.m_staticText211 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer16.Add( self.m_staticText211, 0, wx.ALL, 5 )

		m_comboBox10Choices = []
		self.m_comboBox10 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"LocalAuthListEnabled", wx.DefaultPosition, wx.DefaultSize, m_comboBox10Choices, 0 )
		bSizer16.Add( self.m_comboBox10, 0, wx.TOP|wx.BOTTOM, 5 )

		m_comboBox15Choices = [ u"true", u"false" ]
		self.m_comboBox15 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"true", wx.DefaultPosition, wx.DefaultSize, m_comboBox15Choices, 0 )
		bSizer16.Add( self.m_comboBox15, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button221 = wx.Button( self.m_panel3, wx.ID_ANY, u"傳送本地清單", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button221, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_button28 = wx.Button( self.m_panel3, wx.ID_ANY, u"取得清單版本", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button28, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText22 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"updateType", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer16.Add( self.m_staticText22, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		m_comboBox111Choices = [ u"Full", u"Differential" ]
		self.m_comboBox111 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"Full", wx.DefaultPosition, wx.DefaultSize, m_comboBox111Choices, 0 )
		bSizer16.Add( self.m_comboBox111, 0, wx.TOP|wx.BOTTOM, 5 )


		bSizer19.Add( bSizer16, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button12 = wx.Button( self.m_panel3, wx.ID_ANY, u"觸發訊息", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button12, 0, wx.TOP|wx.BOTTOM, 5 )

		m_comboBox13Choices = [ u"MeterValues", u"Heartbeat", u"StatusNotification", u"DiagnosticsStatusNotification", u"FirmwareStatusNotification", u"BootNotification" ]
		self.m_comboBox13 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"BootNotification", wx.DefaultPosition, wx.DefaultSize, m_comboBox13Choices, 0 )
		bSizer22.Add( self.m_comboBox13, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		bSizer19.Add( bSizer22, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer19 )
		self.m_panel3.Layout()
		bSizer19.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"組態可用性", False )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button13 = wx.Button( self.m_panel4, wx.ID_ANY, u"立即預約", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button13, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText221 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"預約Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		bSizer18.Add( self.m_staticText221, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl15.SetMinSize( wx.Size( 40,-1 ) )

		bSizer18.Add( self.m_textCtrl15, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_button8 = wx.Button( self.m_panel4, wx.ID_ANY, u"取消預約", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button8, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"有效時間", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer18.Add( self.m_staticText23, 0, wx.TOP|wx.BOTTOM, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"預約充電槍", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer18.Add( self.m_staticText18, 0, wx.TOP|wx.BOTTOM, 5 )

		m_comboBox6Choices = [ u"1", u"0", u"-1", u"2", wx.EmptyString ]
		self.m_comboBox6 = wx.ComboBox( self.m_panel4, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox6Choices, 0 )
		bSizer18.Add( self.m_comboBox6, 0, wx.TOP|wx.BOTTOM, 5 )


		self.m_panel4.SetSizer( bSizer18 )
		self.m_panel4.Layout()
		bSizer18.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"預約", False )
		self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText40 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"注意：通常充電樁連線設定ws://IP:port/ocpp/{充電樁的ID}，有些是直接輸入位址，有些充電樁ID是預設或是其他設定欄，有些\"/ocpp\"無法設定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer23.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"安全加密等級1，有些充電樁帳號就是充電樁ID無法設定，Profile2~3需要充電樁先安裝CA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer23.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"OCPP CS啟動：設定IP、Port，加密方式，點選OCPP_CS開啟", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		bSizer23.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"充電程序：插上充電槍->刷卡(ID要正確)->充電-->刷卡-->停止充電(狀態會顯示)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer23.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"更新韌體：需要給定韌體路徑，下載及安裝過程會回報", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		bSizer23.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"取得log：需要給定儲存log路徑(使用ftp_server當路徑，先啟動FTP Server)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		bSizer23.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"傳送Data：需要給定傳送Data路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer23.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"重置：分為Hard/Soft重啟", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		bSizer23.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"預約：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer23.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"變更/設定組態", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		bSizer23.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"變更可用性", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		bSizer23.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.m_staticText39 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"智慧充電", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer23.Add( self.m_staticText39, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer23 )
		self.m_panel5.Layout()
		bSizer23.Fit( self.m_panel5 )
		self.m_notebook1.AddPage( self.m_panel5, u"說明", False )

		bSizer11.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_comboBox1.Bind( wx.EVT_LEFT_DCLICK, self.COM1_NOW )
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.Change_Sec )
		self.m_button111.Bind( wx.EVT_BUTTON, self.UnlockConnector )
		self.m_button101.Bind( wx.EVT_BUTTON, self.OCPP_Link )
		self.m_button15.Bind( wx.EVT_BUTTON, self.RStart_Charging )
		self.m_button16.Bind( wx.EVT_BUTTON, self.RStop_Charging )
		self.m_button9.Bind( wx.EVT_BUTTON, self.Reset )
		self.m_comboBox11.Bind( wx.EVT_LEFT_DCLICK, self.COM2_NOW )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OCPP_Disconnect )
		self.m_button181.Bind( wx.EVT_BUTTON, self.FirmwareUpdate )
		self.m_button271.Bind( wx.EVT_BUTTON, self.SignedFirmwareUpdate )
		self.m_button24.Bind( wx.EVT_BUTTON, self.DataTransfer )
		self.m_button161.Bind( wx.EVT_BUTTON, self.Clear_Slog )
		self.m_button171.Bind( wx.EVT_BUTTON, self.Clear_Rlog )
		self.m_button20.Bind( wx.EVT_BUTTON, self.P1_link )
		self.m_button21.Bind( wx.EVT_BUTTON, self.P2_link )
		self.m_button22.Bind( wx.EVT_BUTTON, self.P3_link )
		self.m_button17.Bind( wx.EVT_BUTTON, self.ChangeConfiguration )
		self.m_button26.Bind( wx.EVT_BUTTON, self.GetConfiguration )
		self.m_button19.Bind( wx.EVT_BUTTON, self.ClearCache )
		self.m_button27.Bind( wx.EVT_BUTTON, self.GetDiagnostics )
		self.m_button14.Bind( wx.EVT_BUTTON, self.SetChargingProfile )
		self.m_button23.Bind( wx.EVT_BUTTON, self.ClearChargingProfile )
		self.m_button25.Bind( wx.EVT_BUTTON, self.GetCompositeSchedule )
		self.m_button18.Bind( wx.EVT_BUTTON, self.ChangeAvailability )
		self.m_button221.Bind( wx.EVT_BUTTON, self.Send_Local_Authorization )
		self.m_button28.Bind( wx.EVT_BUTTON, self.Get_Local_List )
		self.m_button12.Bind( wx.EVT_BUTTON, self.TriggerMessage )
		self.m_button13.Bind( wx.EVT_BUTTON, self.SetReservation )
		self.m_button8.Bind( wx.EVT_BUTTON, self.CancelReservation )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def COM1_NOW( self, event ):
		event.Skip()

	def Change_Sec( self, event ):
		event.Skip()

	def UnlockConnector( self, event ):
		event.Skip()

	def OCPP_Link( self, event ):
		event.Skip()

	def RStart_Charging( self, event ):
		event.Skip()

	def RStop_Charging( self, event ):
		event.Skip()

	def Reset( self, event ):
		event.Skip()

	def COM2_NOW( self, event ):
		event.Skip()

	def OCPP_Disconnect( self, event ):
		event.Skip()

	def FirmwareUpdate( self, event ):
		event.Skip()

	def SignedFirmwareUpdate( self, event ):
		event.Skip()

	def DataTransfer( self, event ):
		event.Skip()

	def Clear_Slog( self, event ):
		event.Skip()

	def Clear_Rlog( self, event ):
		event.Skip()

	def P1_link( self, event ):
		event.Skip()

	def P2_link( self, event ):
		event.Skip()

	def P3_link( self, event ):
		event.Skip()

	def ChangeConfiguration( self, event ):
		event.Skip()

	def GetConfiguration( self, event ):
		event.Skip()

	def ClearCache( self, event ):
		event.Skip()

	def GetDiagnostics( self, event ):
		event.Skip()

	def SetChargingProfile( self, event ):
		event.Skip()

	def ClearChargingProfile( self, event ):
		event.Skip()

	def GetCompositeSchedule( self, event ):
		event.Skip()

	def ChangeAvailability( self, event ):
		event.Skip()

	def Send_Local_Authorization( self, event ):
		event.Skip()

	def Get_Local_List( self, event ):
		event.Skip()

	def TriggerMessage( self, event ):
		event.Skip()

	def SetReservation( self, event ):
		event.Skip()

	def CancelReservation( self, event ):
		event.Skip()


