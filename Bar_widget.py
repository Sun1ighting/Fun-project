# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bar_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SongBar_widget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(514, 331)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 130, 400, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_song_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_song_4.setObjectName("label_song_4")
        self.horizontalLayout_4.addWidget(self.label_song_4)
        self.label_singer_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_singer_4.setObjectName("label_singer_4")
        self.horizontalLayout_4.addWidget(self.label_singer_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_song_4.setText(_translate("Form", "TextLabel"))
        self.label_singer_4.setText(_translate("Form", "TextLabel"))
        self.pushButton_4.setText(_translate("Form", "order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SongBar_widget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())