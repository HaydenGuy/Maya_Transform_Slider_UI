# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transform_sliders.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_transform_sliders(object):
    def setupUi(self, transform_sliders):
        if not transform_sliders.objectName():
            transform_sliders.setObjectName(u"transform_sliders")
        transform_sliders.resize(482, 323)
        font = QFont()
        font.setPointSize(12)
        transform_sliders.setFont(font)
        self.centralwidget = QWidget(transform_sliders)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setContentsMargins(0, -1, 5, -1)
        self.lb_scaleY = QLabel(self.centralwidget)
        self.lb_scaleY.setObjectName(u"lb_scaleY")

        self.gridLayout.addWidget(self.lb_scaleY, 7, 0, 1, 1)

        self.slider_translateY = QSlider(self.centralwidget)
        self.slider_translateY.setObjectName(u"slider_translateY")
        self.slider_translateY.setMinimumSize(QSize(313, 0))
        self.slider_translateY.setMinimum(-100)
        self.slider_translateY.setMaximum(100)
        self.slider_translateY.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_translateY, 1, 2, 1, 1)

        self.lb_translateZ = QLabel(self.centralwidget)
        self.lb_translateZ.setObjectName(u"lb_translateZ")

        self.gridLayout.addWidget(self.lb_translateZ, 2, 0, 1, 1)

        self.lb_scaleZ = QLabel(self.centralwidget)
        self.lb_scaleZ.setObjectName(u"lb_scaleZ")

        self.gridLayout.addWidget(self.lb_scaleZ, 8, 0, 1, 1)

        self.slider_visibility = QSlider(self.centralwidget)
        self.slider_visibility.setObjectName(u"slider_visibility")
        self.slider_visibility.setMaximum(1)
        self.slider_visibility.setPageStep(1)
        self.slider_visibility.setValue(1)
        self.slider_visibility.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_visibility, 9, 2, 1, 1)

        self.slider_scaleZ = QSlider(self.centralwidget)
        self.slider_scaleZ.setObjectName(u"slider_scaleZ")
        self.slider_scaleZ.setMinimumSize(QSize(313, 0))
        self.slider_scaleZ.setMinimum(0)
        self.slider_scaleZ.setMaximum(100)
        self.slider_scaleZ.setSliderPosition(0)
        self.slider_scaleZ.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_scaleZ, 8, 2, 1, 1)

        self.slider_translateZ = QSlider(self.centralwidget)
        self.slider_translateZ.setObjectName(u"slider_translateZ")
        self.slider_translateZ.setMinimumSize(QSize(313, 0))
        self.slider_translateZ.setMinimum(-100)
        self.slider_translateZ.setMaximum(100)
        self.slider_translateZ.setValue(0)
        self.slider_translateZ.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_translateZ, 2, 2, 1, 1)

        self.slider_translateX = QSlider(self.centralwidget)
        self.slider_translateX.setObjectName(u"slider_translateX")
        self.slider_translateX.setMinimumSize(QSize(313, 0))
        self.slider_translateX.setMinimum(-100)
        self.slider_translateX.setMaximum(100)
        self.slider_translateX.setSingleStep(1)
        self.slider_translateX.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_translateX, 0, 2, 1, 1)

        self.lb_rotateX = QLabel(self.centralwidget)
        self.lb_rotateX.setObjectName(u"lb_rotateX")

        self.gridLayout.addWidget(self.lb_rotateX, 3, 0, 1, 1)

        self.slider_rotateX = QSlider(self.centralwidget)
        self.slider_rotateX.setObjectName(u"slider_rotateX")
        self.slider_rotateX.setMinimumSize(QSize(313, 0))
        self.slider_rotateX.setMinimum(-360)
        self.slider_rotateX.setMaximum(360)
        self.slider_rotateX.setValue(0)
        self.slider_rotateX.setSliderPosition(0)
        self.slider_rotateX.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_rotateX, 3, 2, 1, 1)

        self.le_translateX = QLineEdit(self.centralwidget)
        self.le_translateX.setObjectName(u"le_translateX")
        self.le_translateX.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_translateX, 0, 1, 1, 1)

        self.lb_translateX = QLabel(self.centralwidget)
        self.lb_translateX.setObjectName(u"lb_translateX")

        self.gridLayout.addWidget(self.lb_translateX, 0, 0, 1, 1)

        self.slider_scaleY = QSlider(self.centralwidget)
        self.slider_scaleY.setObjectName(u"slider_scaleY")
        self.slider_scaleY.setMinimumSize(QSize(313, 0))
        self.slider_scaleY.setMinimum(0)
        self.slider_scaleY.setMaximum(100)
        self.slider_scaleY.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_scaleY, 7, 2, 1, 1)

        self.slider_rotateZ = QSlider(self.centralwidget)
        self.slider_rotateZ.setObjectName(u"slider_rotateZ")
        self.slider_rotateZ.setMinimumSize(QSize(313, 0))
        self.slider_rotateZ.setMinimum(-360)
        self.slider_rotateZ.setMaximum(360)
        self.slider_rotateZ.setValue(0)
        self.slider_rotateZ.setSliderPosition(0)
        self.slider_rotateZ.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_rotateZ, 5, 2, 1, 1)

        self.slider_rotateY = QSlider(self.centralwidget)
        self.slider_rotateY.setObjectName(u"slider_rotateY")
        self.slider_rotateY.setMinimumSize(QSize(313, 0))
        self.slider_rotateY.setMinimum(-360)
        self.slider_rotateY.setMaximum(360)
        self.slider_rotateY.setValue(0)
        self.slider_rotateY.setSliderPosition(0)
        self.slider_rotateY.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_rotateY, 4, 2, 1, 1)

        self.lb_rotateY = QLabel(self.centralwidget)
        self.lb_rotateY.setObjectName(u"lb_rotateY")

        self.gridLayout.addWidget(self.lb_rotateY, 4, 0, 1, 1)

        self.lb_translateY = QLabel(self.centralwidget)
        self.lb_translateY.setObjectName(u"lb_translateY")

        self.gridLayout.addWidget(self.lb_translateY, 1, 0, 1, 1)

        self.lb_visibility = QLabel(self.centralwidget)
        self.lb_visibility.setObjectName(u"lb_visibility")

        self.gridLayout.addWidget(self.lb_visibility, 9, 0, 1, 1)

        self.lb_rotateZ = QLabel(self.centralwidget)
        self.lb_rotateZ.setObjectName(u"lb_rotateZ")

        self.gridLayout.addWidget(self.lb_rotateZ, 5, 0, 1, 1)

        self.slider_scaleX = QSlider(self.centralwidget)
        self.slider_scaleX.setObjectName(u"slider_scaleX")
        self.slider_scaleX.setMinimumSize(QSize(313, 0))
        self.slider_scaleX.setMinimum(0)
        self.slider_scaleX.setMaximum(100)
        self.slider_scaleX.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_scaleX, 6, 2, 1, 1)

        self.lb_scaleX = QLabel(self.centralwidget)
        self.lb_scaleX.setObjectName(u"lb_scaleX")

        self.gridLayout.addWidget(self.lb_scaleX, 6, 0, 1, 1)

        self.le_translateY = QLineEdit(self.centralwidget)
        self.le_translateY.setObjectName(u"le_translateY")
        self.le_translateY.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_translateY, 1, 1, 1, 1)

        self.le_translateZ = QLineEdit(self.centralwidget)
        self.le_translateZ.setObjectName(u"le_translateZ")
        self.le_translateZ.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_translateZ, 2, 1, 1, 1)

        self.le_rotateX = QLineEdit(self.centralwidget)
        self.le_rotateX.setObjectName(u"le_rotateX")
        self.le_rotateX.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_rotateX, 3, 1, 1, 1)

        self.le_rotateY = QLineEdit(self.centralwidget)
        self.le_rotateY.setObjectName(u"le_rotateY")
        self.le_rotateY.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_rotateY, 4, 1, 1, 1)

        self.le_rotateZ = QLineEdit(self.centralwidget)
        self.le_rotateZ.setObjectName(u"le_rotateZ")
        self.le_rotateZ.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_rotateZ, 5, 1, 1, 1)

        self.le_scaleX = QLineEdit(self.centralwidget)
        self.le_scaleX.setObjectName(u"le_scaleX")
        self.le_scaleX.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_scaleX, 6, 1, 1, 1)

        self.le_scaleY = QLineEdit(self.centralwidget)
        self.le_scaleY.setObjectName(u"le_scaleY")
        self.le_scaleY.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_scaleY, 7, 1, 1, 1)

        self.le_scaleZ = QLineEdit(self.centralwidget)
        self.le_scaleZ.setObjectName(u"le_scaleZ")
        self.le_scaleZ.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_scaleZ, 8, 1, 1, 1)

        self.le_visibility = QLineEdit(self.centralwidget)
        self.le_visibility.setObjectName(u"le_visibility")
        self.le_visibility.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.le_visibility, 9, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        transform_sliders.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(transform_sliders)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 482, 25))
        transform_sliders.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(transform_sliders)
        self.statusbar.setObjectName(u"statusbar")
        transform_sliders.setStatusBar(self.statusbar)

        self.retranslateUi(transform_sliders)

        QMetaObject.connectSlotsByName(transform_sliders)
    # setupUi

    def retranslateUi(self, transform_sliders):
        transform_sliders.setWindowTitle(QCoreApplication.translate("transform_sliders", u"Transform Sliders", None))
        self.lb_scaleY.setText(QCoreApplication.translate("transform_sliders", u"Scale Y:", None))
        self.lb_translateZ.setText(QCoreApplication.translate("transform_sliders", u"Translate Z:", None))
        self.lb_scaleZ.setText(QCoreApplication.translate("transform_sliders", u"Scale Z:", None))
        self.lb_rotateX.setText(QCoreApplication.translate("transform_sliders", u"Rotate X:", None))
        self.lb_translateX.setText(QCoreApplication.translate("transform_sliders", u"Translate X:", None))
        self.lb_rotateY.setText(QCoreApplication.translate("transform_sliders", u"Rotate Y:", None))
        self.lb_translateY.setText(QCoreApplication.translate("transform_sliders", u"Translate Y::", None))
        self.lb_visibility.setText(QCoreApplication.translate("transform_sliders", u"Visibility:", None))
        self.lb_rotateZ.setText(QCoreApplication.translate("transform_sliders", u"Rotate Z:", None))
        self.lb_scaleX.setText(QCoreApplication.translate("transform_sliders", u"Scale X:", None))
    # retranslateUi

