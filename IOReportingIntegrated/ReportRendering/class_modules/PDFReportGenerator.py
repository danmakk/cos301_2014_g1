
from class_modules.ReportGenerator import ReportGenerator
from class_modules.CSVReportGenerator import CSVReportGenerator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import A4

import csv

class PDFReportGenerator(ReportGenerator):
  def __init__(self):		#Constructor
    test = "" #N.B. Remove this line of code when you start
    
  
  csvGen = CSVReportGenerator()
  course_name = 'COS xxx'

  def generateAssessmentReport(self, module, assessment, outputType):  #Assessment Report
    if outputType == "pdf":
      report = self.csvGen.generateAssessmentReport(module, assessment, 'csv')
      self.course_name = module
      print "Test"
      self.create_report(report)
    
  def generateStudentMarksReport(self, module, studentNo, assessments, outputType):  #Student Marks Report
    if outputType == "pdf":
      report = self.csvGen.generateStudentMarksReport(module, studentNo, assessments, 'csv')
      self.course_name = studentNo + ' ' + module
      self.create_report(report)
  
  def generateAuditReport(self, module, userID, alteredTable, dateFrom, dateTo, outputType):  #Audit Report
    if outputType == "pdf":
      report = self.csvGen.generateAuditReport( module, userID, alteredTable, dateFrom, dateTo, 'csv')
      self.course_name = module + ' Audit Report'
      self.create_report(report)

  #testing purposes
  #data_file = 'data20.csv'
  


  def create_report(self,report):
      pdf_name = self.course_name + ' Marksheet.pdf'
      print "Test2"
      fnt = 'Helvetica'
      sz = 12
      
      c = canvas.Canvas(pdf_name, pagesize = landscape(A4)) 
      c.setFont(fnt, sz, leading=None)
      
      heighty = 520
      widthy = 100
      max_width = 800
      width_dec = 30
      
      
      #header text
      c.drawCentredString(110, 550, self.course_name + ' Marksheet')
      c.drawCentredString(800, 550, 'H')
      
      #tmp_data = csv.reader(open(report, "rb"))
      tmp_data = csv.reader(report)
      hdngs = next(tmp_data)
      num_cols = len(hdngs)
      
      if num_cols > 35:
          width_dec = 600/num_cols
          sz = 8
          c.setFont(fnt, sz, leading=None)
      elif num_cols > 20:
          width_dec = 600/num_cols
          sz = 10
          c.setFont(fnt, sz, leading=None)
      
      
      #print num_cols
      
      #marks_data = csv.reader(open(report, "rb"))
      marks_data = csv.reader(report)
      for row in marks_data:
          
          heighty -= 20
          
          c.drawCentredString(widthy, heighty, row[0])
          widthy += 70
          
          for k in range(1, num_cols):
              c.drawCentredString(widthy, heighty, row[k])
              widthy += width_dec
              
          widthy = 100
          
          if heighty < 50:
              c.showPage()
              heighty = 550
              c.setFont(fnt, sz, leading=None)
      print "Test3"    
      #save pdf page, use for each page
      c.showPage()
      #print 'created'
      c.save()
      return c