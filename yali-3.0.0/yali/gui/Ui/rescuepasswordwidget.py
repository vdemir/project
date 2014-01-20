# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yali/gui/Ui/rescuepasswordwidget.ui'
#
# Created: Mon Jan 20 02:08:33 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import gettext
__trans = gettext.translation('yali', fallback=True)
i18n = __trans.ugettext
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RescuePasswordWidget(object):
    def setupUi(self, RescuePasswordWidget):
        RescuePasswordWidget.setObjectName(_fromUtf8("RescuePasswordWidget"))
        RescuePasswordWidget.resize(782, 519)
        self.gridLayout = QtGui.QGridLayout(RescuePasswordWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(RescuePasswordWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(600, 250))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame.setStyleSheet(_fromUtf8("#frame{\n"
"background-color: rgba(0, 0, 0, 20);\n"
"border-top: 1px solid rgba(255, 255, 255, 75);/*white*/\n"
"border-bottom: 1px solid rgba(255, 255, 255, 75);/*white*/\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"QListView {\n"
"show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
" }\n"
"\n"
"QListView{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-radius:2px;\n"
"color:white;\n"
"}\n"
"\n"
"QListView::item {\n"
"border-radius:2;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0));\n"
"color: rgb(220, 220, 220);\n"
"padding:5\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"border-radius:2;\n"
"color:white;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"border-radius:2;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"color:white;\n"
"}\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(203, 239, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.infoLabel = QtGui.QLabel(self.frame)
        self.infoLabel.setStyleSheet(_fromUtf8(""))
        self.infoLabel.setWordWrap(False)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.verticalLayout.addWidget(self.infoLabel)
        self.users = QtGui.QListWidget(self.frame)
        self.users.setMaximumSize(QtCore.QSize(16777215, 100))
        self.users.setObjectName(_fromUtf8("users"))
        self.verticalLayout.addWidget(self.users)
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.confirmLabel = QtGui.QLabel(self.groupBox)
        self.confirmLabel.setWordWrap(False)
        self.confirmLabel.setObjectName(_fromUtf8("confirmLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.confirmLabel)
        self.password = QtGui.QLineEdit(self.groupBox)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.password)
        self.passwordLabel = QtGui.QLabel(self.groupBox)
        self.passwordLabel.setWordWrap(False)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.resetPassword = QtGui.QPushButton(self.groupBox)
        self.resetPassword.setEnabled(True)
        self.resetPassword.setFlat(False)
        self.resetPassword.setObjectName(_fromUtf8("resetPassword"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.resetPassword)
        self.confirm = QtGui.QLineEdit(self.groupBox)
        self.confirm.setEchoMode(QtGui.QLineEdit.Password)
        self.confirm.setObjectName(_fromUtf8("confirm"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.confirm)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(225, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(RescuePasswordWidget)
        QtCore.QMetaObject.connectSlotsByName(RescuePasswordWidget)

    def retranslateUi(self, RescuePasswordWidget):
        self.infoLabel.setText(i18n("Choose the user you want to reset the password:"))
        self.confirmLabel.setText(i18n("Password:"))
        self.passwordLabel.setText(i18n("Confirm Password"))
        self.resetPassword.setText(i18n("Reset Password"))

