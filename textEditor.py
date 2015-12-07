<<<<<<< HEAD
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyHighlighter( QSyntaxHighlighter ):

    def __init__( self, parent, theme ):
      QSyntaxHighlighter.__init__( self, parent )
      self.parent = parent
      keyword = QTextCharFormat()
      reservedClasses = QTextCharFormat()
      assignmentOperator = QTextCharFormat()
      delimiter = QTextCharFormat()
      specialConstant = QTextCharFormat()
      boolean = QTextCharFormat()
      number = QTextCharFormat()
      comment = QTextCharFormat()
      string = QTextCharFormat()
      singleQuotedString = QTextCharFormat()

      self.highlightingRules = []

      # keyword
      brush = QBrush( Qt.blue, Qt.SolidPattern )
      keyword.setForeground( brush )
      keyword.setFontWeight( QFont.Bold )
      keywords = QStringList(["LIKE", "BLOCK", "FOLLOW", "REPLY",
                                "TWEET", "UNFOLLOW", "ELSE", "IF", "RT", "ELSEIF"] )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, keyword )
        self.highlightingRules.append( rule )

      brush = QBrush( Qt.yellow, Qt.SolidPattern )
      pattern = QRegExp( "(<){1,2}-" )
      assignmentOperator.setForeground( brush )
      assignmentOperator.setFontWeight( QFont.Bold )
      rule = HighlightingRule( pattern, assignmentOperator )
      self.highlightingRules.append( rule )

      pattern = QRegExp( "[\)\(]+|[\{\}]+|[][]+" )
      delimiter.setForeground( brush )
      delimiter.setFontWeight( QFont.Bold )
      rule = HighlightingRule( pattern, delimiter )
      self.highlightingRules.append( rule )

      brush = QBrush( Qt.green, Qt.SolidPattern )
      specialConstant.setForeground( brush )
      keywords = QStringList( [ "INT", "TRALSE", "COKE", "CHIRP", "MSG", "LOGIN", "LOGOUT" ] )
      for word in keywords:
        pattern = QRegExp("@" + word + "\\b")
        rule = HighlightingRule( pattern, specialConstant )
        self.highlightingRules.append( rule )

      # boolean
      boolean.setForeground( brush )
      keywords = QStringList( [ "YES", "NO" ] )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, boolean )
        self.highlightingRules.append( rule )

      # number
      pattern = QRegExp( "[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?" )
      pattern.setMinimal( True )
      number.setForeground( brush )
      rule = HighlightingRule( pattern, number )
      self.highlightingRules.append( rule )

      # comment
      brush = QBrush( Qt.blue, Qt.SolidPattern )
      pattern = QRegExp( "#[^\n]*" )
      comment.setForeground( brush )
      rule = HighlightingRule( pattern, comment )
      self.highlightingRules.append( rule )

      # string
      brush = QBrush( Qt.red, Qt.SolidPattern )
      pattern = QRegExp( "\".*\"" )
      pattern.setMinimal( True )
      string.setForeground( brush )
      rule = HighlightingRule( pattern, string )
      self.highlightingRules.append( rule )

      # singleQuotedString
      pattern = QRegExp( "\'.*\'" )
      pattern.setMinimal( True )
      singleQuotedString.setForeground( brush )
      rule = HighlightingRule( pattern, singleQuotedString )
      self.highlightingRules.append( rule )

    def highlightBlock( self, text ):
      for rule in self.highlightingRules:
        expression = QRegExp( rule.pattern )
        index = expression.indexIn( text )
        while index >= 0:
          length = expression.matchedLength()
          self.setFormat( index, length, rule.format )
          index = text.indexOf( expression, index + length )
      self.setCurrentBlockState( 0 )

class HighlightingRule():
  def __init__( self, pattern, format ):
    self.pattern = pattern
    self.format = format

class TestApp( QMainWindow ):
  def __init__(self):
    QMainWindow.__init__(self)
    font = QFont()
    font.setFamily( "Courier" )
    font.setFixedPitch( True )
    font.setPointSize( 10 )
    editor = QTextEdit()
    editor.setFont( font )
    highlighter = MyHighlighter( editor, "Classic" )
    self.setCentralWidget( editor )
    self.setWindowTitle( "Text Editor for CS 150" )
    self.initUI()

  def initUI(self):

    newAction = QAction('New', self)
    newAction.setShortcut('Ctrl+N')
    newAction.triggered.connect(self.newFile)

    saveAction = QAction('New', self)
    saveAction.setShortcut('Ctrl+S')
    saveAction.triggered.connect(self.saveFile)

    openAction = QAction('Open', self)
    openAction.setShortcut('Ctrl+O')
    openAction.triggered.connect(self.openFile)

    menubar = self.menuBar()
    fileMenu = menubar.addMenu('File')
    fileMenu.addAction(newAction)
    fileMenu.addAction(saveAction)
    fileMenu.addAction(openAction)

    self.show()

  
  def newFile(self):
    self.txt.clea()

  def saveFile(self):
    filename = QFileDialog.getSaveFileName(self, 'Save File')
    f = open(filename, 'w')
    filedata = self.twt.toPlainText()
    f.write(filedata)
    f.close()


  def openFile(self):
    filename = QFileDialog.getOpenFileName(self, 'Open File')
    f = open(filename, 'r')
    filedata = f.read()
    self.txt.setText(filedata)
    f.close()

if __name__ == "__main__":
  app = QApplication( sys.argv )
  window = TestApp()
  window.show()
  sys.exit( app.exec_() )
=======
from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveAs():
	f = asksaveasfile(mode='w', defaultextension='.twt')
	t = text.fet(0.0, END)
	try:
		f.write(t.rstrip())
	except:

		showerror(title="Error!", message="File can not be saved.")
def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

root = Tk()
root.title("Text Editor for CS 150")
root.minsize(width=400, height=400)
root.maxsize(width=1280, height=720)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
>>>>>>> 18952a32d51f2ca1ae493b0ac475a60938fd08c6
