import sys
import maya.cmds as cmds
import maya.OpenMaya as om

from PySide6.QtWidgets import QMainWindow, QApplication

import Maya_Transform_Slider_UI.UI.ui as ui

class TransformSliders(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ui.Ui_transform_sliders()
        self.ui.setupUi(self)

        # Initialises the slider values based on the selected object
        self.value_update()

        # Calls Maya's scriptJob to run selection_changed if the 'SelectionChanged' event occurs
        self.selection_changed_update = cmds.scriptJob(
            e=['SelectionChanged', self.selection_changed])

        # Connection the sliders values changing to the transform update
        self.ui.slider_translateX.valueChanged.connect(self.slider_update)
        self.ui.slider_translateY.valueChanged.connect(self.slider_update)
        self.ui.slider_translateZ.valueChanged.connect(self.slider_update)
        self.ui.slider_rotateX.valueChanged.connect(self.slider_update)
        self.ui.slider_rotateY.valueChanged.connect(self.slider_update)
        self.ui.slider_rotateZ.valueChanged.connect(self.slider_update)
        self.ui.slider_scaleX.valueChanged.connect(self.slider_update)
        self.ui.slider_scaleY.valueChanged.connect(self.slider_update)
        self.ui.slider_scaleZ.valueChanged.connect(self.slider_update)
        self.ui.slider_visibility.valueChanged.connect(self.slider_update)

        self.ui.le_translateX.textChanged.connect(self.text_update)
        self.ui.le_translateY.textChanged.connect(self.text_update)
        self.ui.le_translateZ.textChanged.connect(self.text_update)
        self.ui.le_rotateX.textChanged.connect(self.text_update)
        self.ui.le_rotateY.textChanged.connect(self.text_update)
        self.ui.le_rotateZ.textChanged.connect(self.text_update)
        self.ui.le_scaleX.textChanged.connect(self.text_update)
        self.ui.le_scaleY.textChanged.connect(self.text_update)
        self.ui.le_scaleZ.textChanged.connect(self.text_update)
        self.ui.le_visibility.textChanged.connect(self.text_update)

    # Gets the selected object and assigns a transform based on the slider value of the selected slider
    def slider_update(self, value):
        selected_object = cmds.ls(selection=True, type="transform")
        slider_name = self.sender().objectName()
        slider_transform = slider_name[7:]

        for obj in selected_object:
            cmds.setAttr(obj + f".{slider_transform}", value)

        self.value_update()

    # Gets the selected object and assigns a transform based on the line edit input value
    def text_update(self, value):
        selected_object = cmds.ls(selection=True, type="transform")
        line_edit_name = self.sender().objectName()
        line_edit_transform = line_edit_name[3:]
        
        # If the user inputs anything except an integer an error is raised
        try:
            for obj in selected_object:
                cmds.setAttr(obj + f".{line_edit_transform}", int(value))
                self.value_update()
        except ValueError:
            om.MGlobal.displayError("Enter an integer value")

    # Updates the slider and text values based on the current values
    def value_update(self):
        selected_object = cmds.ls(selection=True, type="transform")
        object = selected_object[0]

        translateX = cmds.getAttr(object + ".translateX")
        translateY = cmds.getAttr(object + ".translateY")
        translateZ = cmds.getAttr(object + ".translateZ")
        rotateX = cmds.getAttr(object + ".rotateX")
        rotateY = cmds.getAttr(object + ".rotateY")
        rotateZ = cmds.getAttr(object + ".rotateZ")
        scaleX = cmds.getAttr(object + ".scaleX")
        scaleY = cmds.getAttr(object + ".scaleY")
        scaleZ = cmds.getAttr(object + ".scaleZ")
        visibility = cmds.getAttr(object + ".visibility")

        self.ui.le_translateX.setText(f"{int(translateX)}")
        self.ui.le_translateY.setText(f"{int(translateY)}")
        self.ui.le_translateZ.setText(f"{int(translateZ)}")
        self.ui.le_rotateX.setText(f"{int(rotateX)}")
        self.ui.le_rotateY.setText(f"{int(rotateY)}")
        self.ui.le_rotateZ.setText(f"{int(rotateZ)}")
        self.ui.le_scaleX.setText(f"{int(scaleX)}")
        self.ui.le_scaleY.setText(f"{int(scaleY)}")
        self.ui.le_scaleZ.setText(f"{int(scaleZ)}")
        self.ui.le_visibility.setText(f"{int(visibility)}")

        self.ui.slider_translateX.setValue(int(translateX))
        self.ui.slider_translateY.setValue(int(translateY))
        self.ui.slider_translateZ.setValue(int(translateZ))
        self.ui.slider_rotateX.setValue(int(rotateX))
        self.ui.slider_rotateY.setValue(int(rotateY))
        self.ui.slider_rotateZ.setValue(int(rotateZ))
        self.ui.slider_scaleX.setValue(int(scaleX))
        self.ui.slider_scaleY.setValue(int(scaleY))
        self.ui.slider_scaleZ.setValue(int(scaleZ))
        self.ui.slider_visibility.setValue(visibility)

    # If the selection changes the slider numbers are updated
    def selection_changed(self):
        self.value_update()


if __name__ == '__main__':
    # Create a Qt application instance or use the existing one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    # Create an instance of the main window
    window = TransformSliders()
    window.show()