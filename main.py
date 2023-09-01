import sys
import maya.cmds as cmds

sys.path.append(
    '/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya_Scripts/Transform_Sliders')

from PySide2.QtWidgets import QMainWindow, QApplication
from UI.Ui_transform_sliders import Ui_transform_sliders

class TransformSliders(QMainWindow, Ui_transform_sliders):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialises the slider values based on the selected object
        self.value_update()

        # Calls Maya's scriptJob to run selection_changed if the 'SelectionChanged' event occurs
        self.selection_changed_update = cmds.scriptJob(
            e=['SelectionChanged', self.selection_changed])

        # Connection the sliders values changing to the transform update
        self.slider_translateX.valueChanged.connect(self.transform_update)
        self.slider_translateY.valueChanged.connect(self.transform_update)
        self.slider_translateZ.valueChanged.connect(self.transform_update)
        self.slider_rotateX.valueChanged.connect(self.transform_update)
        self.slider_rotateY.valueChanged.connect(self.transform_update)
        self.slider_rotateZ.valueChanged.connect(self.transform_update)
        self.slider_scaleX.valueChanged.connect(self.transform_update)
        self.slider_scaleY.valueChanged.connect(self.transform_update)
        self.slider_scaleZ.valueChanged.connect(self.transform_update)
        self.slider_visibility.valueChanged.connect(self.transform_update)

    # Gets the selected object and assigns a transform based on the slider value of the selected slider
    def transform_update(self, value):
        selected_object = cmds.ls(selection=True, type="transform")
        slider_name = self.sender().objectName()
        slider_transform = slider_name[7:]

        for obj in selected_object:
            cmds.setAttr(obj + f".{slider_transform}", value)

        self.value_update()

    # Updates the slider values based on the current value of the slider
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

        self.value_translateX.setText(f"{int(translateX)}")
        self.value_translateY.setText(f"{int(translateY)}")
        self.value_translateZ.setText(f"{int(translateZ)}")
        self.value_rotateX.setText(f"{int(rotateX)}")
        self.value_rotateY.setText(f"{int(rotateY)}")
        self.value_rotateZ.setText(f"{int(rotateZ)}")
        self.value_scaleX.setText(f"{int(scaleX)}")
        self.value_scaleY.setText(f"{int(scaleY)}")
        self.value_scaleZ.setText(f"{int(scaleZ)}")
        self.value_visibility.setText(f"{int(visibility)}")

        self.slider_translateX.setValue(int(translateX))
        self.slider_translateY.setValue(int(translateY))
        self.slider_translateZ.setValue(int(translateZ))
        self.slider_rotateX.setValue(int(rotateX))
        self.slider_rotateY.setValue(int(rotateY))
        self.slider_rotateZ.setValue(int(rotateZ))
        self.slider_scaleX.setValue(int(scaleX))
        self.slider_scaleY.setValue(int(scaleY))
        self.slider_scaleZ.setValue(int(scaleZ))
        self.slider_visibility.setValue(visibility)

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
    # Show the main window
    window.show()