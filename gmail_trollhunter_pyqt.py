from PyQt6.QtCore import QSize, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys
import helper_funcs as gth

class MainWindow(QMainWindow):
    graph_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.max_results = None
        self.sortedcounts = None

        self.setWindowTitle("Gmail Trollhunter")
        self.setFixedSize(QSize(1000,550))
        self.layout=QVBoxLayout()

        description = QLabel("Check out which senders are spamming you with lots of emails.")
        text_font = description.font()
        text_font.setPointSize(20)
        description.setFont(text_font)
        description.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        email_entry_description = QLabel("How many emails would you like to check?")
        email_entry_description.setFont(text_font)
        email_entry_description.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        email_entry = QLineEdit()
        email_entry.setPlaceholderText("Enter number here...")
        email_entry.textChanged.connect(self.new_max_results)
        email_entry.returnPressed.connect(self.the_button_was_pressed)

        self.button = QPushButton("Find your Trolls!")
        # self.button.setFixedSize(QSize(800,600))
        # button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_pressed)
        self.graph_signal.connect(self.the_graph_appeared)
        
        self.graph = QLabel(self)
        self.graph.setScaledContents(True)

        self.layout.addWidget(description)
        self.layout.addWidget(email_entry_description)
        self.layout.addWidget(email_entry)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.graph)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def the_button_was_pressed(self):
        print("Pressed!")
        if self.max_results == None:
            print("Enter a value for max_results!")
        else:
            self.button.setText("Running..")
            self.button.setEnabled(False)
            print(self.max_results)
            self.sortedcounts = gth.getEmails(sortedcounts=self.sortedcounts, max_results=int(self.max_results))
            gth.plot_sorted_counts(self.sortedcounts)
            self.graph_signal.emit()

    def new_max_results(self, s):
        self.max_results = s

    def the_graph_appeared(self):
        pixmap = QPixmap('sortedcounts.png')
        self.graph.setPixmap(pixmap)
        self.button.setEnabled(True)
        self.button.setText("Find more Trolls!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())