from PySide import QtCore, QtGui

class PropulsionFrame(QtGui.QGroupBox):
    """A widget to display information about the propulsion system."""

    def __init__(self, parent):
        """Create and initialize a PropulsionFrame.

        Args:
            parent (QWidget): Parent Qt widget.
        """
        super(PropulsionFrame, self).__init__('Propulsion', parent)

        self._initUI()

    def _initUI(self):
        """A private method to initalize the UI."""
        # Create main layout
        propulsion_layout = QtGui.QHBoxLayout()
        self.setLayout(propulsion_layout)

        # Create space on left to center the widgets
        propulsion_layout.addStretch(1)

        # Create a grid layout to contain bar widgets
        propulsion_grid = QtGui.QGridLayout()
        propulsion_layout.addLayout(propulsion_grid)

        # Left and right speed indicators
        self.left_speed_bar = QtGui.QProgressBar(self)
        self.left_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.left_speed_bar.setTextVisible(True)
        self.left_speed_bar.setMinimum(0)
        self.left_speed_bar.setMaximum(255)
        self.left_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.left_speed_bar, 0, 2, 3, 1)
        self.right_speed_bar = QtGui.QProgressBar(self)
        self.right_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.right_speed_bar.setTextVisible(True)
        self.right_speed_bar.setMinimum(0)
        self.right_speed_bar.setMaximum(255)
        self.right_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.right_speed_bar, 0, 3, 3, 1)

        # Wheel speed indicators
        self.m1_speed_bar = QtGui.QProgressBar(self)
        self.m1_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.m1_speed_bar.setTextVisible(True)
        self.m1_speed_bar.setMinimum(0)
        self.m1_speed_bar.setMaximum(255)
        self.m1_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.m1_speed_bar, 0, 1, 1, 1)
        self.m2_speed_bar = QtGui.QProgressBar(self)
        self.m2_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.m2_speed_bar.setTextVisible(True)
        self.m2_speed_bar.setMinimum(0)
        self.m2_speed_bar.setMaximum(255)
        self.m2_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.m2_speed_bar, 1, 1, 1, 1)
        self.m3_speed_bar = QtGui.QProgressBar(self)
        self.m3_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.m3_speed_bar.setTextVisible(True)
        self.m3_speed_bar.setMinimum(0)
        self.m3_speed_bar.setMaximum(255)
        self.m3_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.m3_speed_bar, 2, 1, 1, 1)
        self.m4_speed_bar = QtGui.QProgressBar(self)
        self.m4_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.m4_speed_bar.setTextVisible(True)
        self.m4_speed_bar.setMinimum(0)
        self.m4_speed_bar.setMaximum(255)
        self.m4_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.m4_speed_bar, 0, 4, 1, 1)
        self.m5_speed_bar = QtGui.QProgressBar(self)
        self.m5_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.m5_speed_bar.setTextVisible(True)
        self.m5_speed_bar.setMinimum(0)
        self.m5_speed_bar.setMaximum(255)
        self.m5_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.m5_speed_bar, 1, 4, 1, 1)
        self.m6_speed_bar = QtGui.QProgressBar(self)
        self.m6_speed_bar.setOrientation(QtCore.Qt.Vertical)
        self.m6_speed_bar.setTextVisible(True)
        self.m6_speed_bar.setMinimum(0)
        self.m6_speed_bar.setMaximum(255)
        self.m6_speed_bar.setValue(128)
        propulsion_grid.addWidget(self.m6_speed_bar, 2, 4, 1, 1)

        # Wheel steering indicators
        self.s1_dial = QtGui.QDial(self)
        self.s1_dial.setMinimum(-90)
        self.s1_dial.setMaximum(90)
        self.s1_dial.setValue(0)
        propulsion_grid.addWidget(self.s1_dial, 0, 0, 1, 1)
        self.s3_dial = QtGui.QDial(self)
        self.s3_dial.setMinimum(-90)
        self.s3_dial.setMaximum(90)
        self.s3_dial.setValue(0)
        propulsion_grid.addWidget(self.s3_dial, 2, 0, 1, 1)
        self.s4_dial = QtGui.QDial(self)
        self.s4_dial.setMinimum(-90)
        self.s4_dial.setMaximum(90)
        self.s4_dial.setValue(0)
        propulsion_grid.addWidget(self.s4_dial, 0, 5, 1, 1)
        self.s6_dial = QtGui.QDial(self)
        self.s6_dial.setMinimum(-90)
        self.s6_dial.setMaximum(90)
        self.s6_dial.setValue(0)
        propulsion_grid.addWidget(self.s6_dial, 2, 5, 1, 1)

        # Create space on right to center the widgets
        propulsion_layout.addStretch(1)
