from django.conf.urls import patterns, include, url
from views import *
from Android import userUrls, studentUrls, markerUrls
import sys

import csv

urlpatterns = patterns('',
	#home page
	(r'^logout/$', logout),
	(r'^$', loginWeb),
	(r'^index/$', loginWeb),
	(r'^getCourseAssessments/$', getCourseAssessments),
	(r'^getAssessmentsOptions/$', viewAssessmentsOptions),
	(r'^getAssessmentSessionsOptions/$', viewAssessmentSessionsOptions),
	(r'^getSessionStudentMarks/$', getSessionStudentMarks),
	(r'^student/(?P<course>\w{6})/(?P<assessment>[0-9]+)/$', studentPage),
	(r'^tutor/(?P<course>\w{6})/(?P<assessment>[0-9]+)/$', tutorPage),
	(r'^teachingAssistant/(?P<course>\w{6})/(?P<assessment>[0-9]+)/$', teachingAssistantPage),
	(r'^lecturer/(?P<course>\w{6})/(?P<assessment>[0-9]+)/$', lecturerPage),
	
	(r'^assessmentView/$', assessment_view),
	(r'^test/$', test),
	(r'^marks-management/$', marks_management),
	url(r'^Android/User/',include(userUrls)),
	url(r'^Android/Student/',include(studentUrls)),
	url(r'^Android/Marker/',include(markerUrls)),
	(r'^ldapTest/$', ldapTest),
	(r'^importTest/$', importTest),
	(r'^AssReportTestTest/$', AssReportTest),
	(r'^studReportTest/$', studReportTest),
	(r'^auditReportTest/$', auditReportTest),

	#student report page
	#~ (r'^studentReport/$', studentReport),
	#~ #audit report page
	#~ (r'^auditReport/$', auditReport),
	#~ #marker home page
	#~ (r'^marker/$', marker_home),
	#assessments view
	#(r'^assessmentView/$', assessment_view),
	#manage assessments
	(r'^assessmentManager/$', AssessmentManager),
	#~ #manage sessions
	#(r'^sessionManager/$', session_manager),
	#~ #view audit report
	###(r'^auditReport/$', view_audit_report),
	#~ #reporting mani menu
	###(r'^Reporting_Main/$', reporting_main),
	#~ #statistics
	#(r'^Statistics/$', statistics),
	#~ #all students
	#~ (r'^students/$', view_all_students),
	#~ #view individual student
	#~ (r'^student/(?P<studentNumber>\w{1}\d{8})/$', view_student),
	#(r'^studentReport/$', student_report),
	(r'^publish/$', publish),
	#(r'^marks-management/$', marks_management),
	#~ #view individual course
	#~ (r'^course/(?P<courseCode>\w{3}\d{3})/$', view_course),
	#~ #view all courses
	#~ (r'^courses/$', view_all_course),
	
	(r'^auditReport/$', audit_report),
	(r'^Reporting_Main/$', reporting_main),
	#~ (r'^Statistics/$', statistics),
	(r'^studentChosen/$', student_chosen),

	(r'^studentReport/$', student_report),

        (r'^assessmentReport/$', assessmentReport),

	(r'^marks-management/$', marks_management),

        (r'^frequency_analysis/$', frequency_analysis),

        #(r'^get_module_mark/$', get_module_mark),

        (r'^getAssessments/$', getAssessments),

        (r'^getLeafAssessments/$', getLeafAssessments),

        (r'^getLecturerModules/$', getLecturerModules),

        (r'^studentModules/$', studentModules),

        (r'^searchStudents/$', searchStudents),

        (r'^displayStudent/$', displayStudent),

        (r'^generateAuditLog/$', generate_auditLog),

        (r'^getStatistics/$', get_statistics),
        (r'^renderPDF/$', renderPDF),

	(r'^renderCSV/$', renderCSV),
	(r'^assessment/lecturer$', lecturer_assessment),
)
