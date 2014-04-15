from django.db import models
import time                     # [jacques] For audit logging
import datetime
from SquirrelMarking.ldapView import *
class Person:
    firstName = ""
    upId = ""
    surname = ""
    studentOf  = [] #module
    tutorOf  = [] #module
    teachingAssistantOf  = [] #module
    lectureOf = []
    def _init_(self,fn, sn, uid):
        self.firstName = fn
        self.upId = uid
        self.surname = sn
    def getfirstName(self):
        return self.firstName
    def getupId(self):
        return self.upId
    def getsurname(self):
        return self.surname
    def setfirstName(self,value):
        self.firstName=value
    def setupId(self,value):
        self.upId=value
    def setsurname(self,value):
        self.surname=value
    def lectureOfInsert(self,value):
        self.lectureOf.append(value)
    def lectureOfDelete(self,value):
        self.lectureOf.remove(value)
    def studentOfInsert(self,value):
        self.studentOf.append(value)
    def studentOfDelete(self,value):
        self.studentOf.remove(value)
    def tutorOfInsert(self,value):
        self.tutorOf.append(value)
    def tutorOfDelete(self,value):
        self.tutorOf.remove(value)
    def teachingAssistantOfInsert(self,value):
        self.teachingAssistantOf.append(value)
    def teachingAssistantOfDelete(self,value):
        self.teachingAssistantOf.remove(value)
    def __unicode__(self):
        return self.getfirstName()+" "+self.getsurname()+" "+self.getupId()

def getPersonFromArr(data):
    objPerson = Person()
    objPerson.setfirstName(data["cn"])
    objPerson.setsurname(data["sn"])
    objPerson.setupId(data["uid"])
    #objPerson = Person(data["cn"],data["sn"],data["uid"])

    for x in data["studentOf"]:
        objPerson.studentOfInsert(x)

    for x in data["tutorFor"]:
        objPerson.tutorOfInsert(x)

    for x in data["teachingAssistantOf"]:
        objPerson.teachingAssistantOfInsert(x)

    for x in data["lecturerOf"]:
        objPerson.lectureOfInsert(x)

    return objPerson


class Module(models.Model):
    code=models.CharField(max_length=100,primary_key=True)
    def getModuleCode()
	return code
    def __unicode__(self):
        return self.code

def deleteModule(self):
    Module.delete(self)

def insertModule(code_):
    temp = Module(code=code_)
    temp.save()
    return temp

def getModule():
    temp=Module.objects.all()
    return temp

class Assessment(models.Model):
    assessment_name=models.CharField(max_length=100)
    assessment_weight=models.CharField(max_length=100)
    assessment_type=models.CharField(max_length=100)
    module_id =models.ForeignKey(Module)

    def setName(self,name):
        self.assessment_name = name
    def setWeight(self,weight):
        self.assessment_weight = weight
    def setType(self,type):
        self.assessment_type = type
    def setModule(self,module):
        self.module_id = module
    def getID(self):
        return self.id
    def getName(self):
        return self.assessment_name
    def getWeight(self):
        return self.assessment_weight
    def getType(self):
        return self.assessment_type
    def getModule(self):
        return self.module_id
    def __unicode__(self):
        return self.assessment_name
def deleteAssessment(self):
    Assessment.delete(self)

def insertAssessment(assessment_name_,assessment_weight_,assessment_type_,module_id_):
    temp = Assessment(assessment_name=assessment_name_,assessment_weight=assessment_weight_,assessment_type=assessment_type_,module_id=module_id_)
    temp.save()
    return temp

def getAssessment():
    temp=Assessment.objects.all()
    return temp


class Sessions(models.Model):
    session_name=models.CharField(max_length=100)
    assessment_id = models.ForeignKey(Assessment)
    opened = models.DateTimeField()
    closed = models.DateTimeField()
    status = models.IntegerField()
    def setAssessmentID(self,id):
        self.assessment_id = id
    def setOpen(self):
        self.status = 1
    def setClosed(self):
        self.status = 2
    def setName(self,name):
        self.session_name = name
    #getters
    def __unicode__(self):
        return self.session_name
    def getID(self):
        return self.id
    def getAssessmentID(self):
        return self.assessment_id
    def getClosed(self):
        return self.closed
    def getStatus(self):
        return self.status
    def getOpen(self):
        return self.open

def deleteSessions(self):
    Sessions.delete(self)

def insertSessions(assessment_id_,open_,closed_):
    temp = Sessions(assessment_id=assessment_id_,open=open_,closed=closed_,status=0)
    temp.save()
    return temp

def getSessions():
    temp=Sessions.objects.all()
    return temp

class MarkerSessions(models.Model):
    marker_id=models.CharField(max_length=100)
    session_id= models.ForeignKey(Sessions)
    def setMarker(self, marker):
        self.marker_id = marker
    def setID(self,id):
        self.session_id = id

    def getMarker(self):
        return self.marker_id
    def getID(self):
        return self.session_id
    def __unicode__(self):
        return "MarkerSessions"


def deleteMarkerSessions(self):
    MarkerSessions.delete(self)

def insertMarkSession(marker_id_,session_id_):
    temp = MarkerSessions(marker_id=marker_id_,session_id=session_id_)
    temp.save()
    return temp

def getMarkerSessions():
    temp=MarkerSessions.objects.all()
    return temp

class MarkerModule(models.Model):
    marker_id=models.CharField(max_length=100)
    module= models.ForeignKey(Module)
    def __unicode__(self):
        return "MarkerModule"
def deleteMarkerModule(self):
    MarkerModule.delete(self)

def insertMarkerModule(marker_id_,module_):
    temp = MarkerModule(marker_id=marker_id_,module=module_)
    temp.save()
    return temp

def getMarkerModule():
    temp=MarkerModule.objects.all()
    return temp

class LeafAssessment(models.Model):
    leaf_name=models.CharField(max_length=100)
    assessment_id = models.ForeignKey(Assessment)
    max_mark = models.IntegerField()
    published = models.BooleanField()

    def setName(self,name):
        self.leaf_name = name
    def setAssessment_id(self,id):
        self.assessment_id = id
    def setMax_mark(self,mark):
        self.max_mark = mark
    def setPublished(self,pub):
        self.published = pub
    def getID(self):
        return self.id
    def getName(self):
        return self.leaf_name
    def getAssessment_id(self):
        return self.assessment_id
    def getMax_mark(self):
        return self.max_mark
    def getPublished(self):
        return self.published
    def __unicode__(self):
        return self.leaf_name

def deleteLeafAssessment(self):
    LeafAssessment.delete(self)

def insertLeafAssessment(leaf_name_,assessment_id_,max_mark_,published_):
    temp = LeafAssessment(leaf_name=leaf_name_,assessment_id=assessment_id_,max_mark=max_mark_,published=published_)
    temp.save()
    return temp

def getLeafAssessment():
    temp=LeafAssessment.objects.all()
    return temp

class MarkAllocation(models.Model):
    leaf_id = models.ForeignKey(LeafAssessment)
    mark = models.IntegerField()
    session_id =models.ForeignKey(Sessions)
    marker =models.CharField(max_length=100)
    student=models.CharField(max_length=100)
    timeStamp = models.DateTimeField()

    def setLeaf_id(self,id):
        self.leaf_id = id
    def setMark(self,_mark):
        self.mark = _mark
    def setSession_id(self,id):
        self.session_id = id
    def setMarker(self,_marker):
        self.marker = _marker
    def setStudent(self,_student):
        self.student = _student
    def setTimeStamp(self,time):
        self.timeStamp= time

    def getID(self):
        return self.id
    def getLeaf_id(self):
        return self.leaf_id
    def getMark(self):
        return self.mark
    def getSession_id(self):
        return self.session_id
    def getMarker(self):
        return self.marker
    def getStudent(self):
        return self.student
    def getTimeStamp(self):
        return self.timeStamp
    def __unicode__(self):
        return "MarkAllocation"

def deleteMarkAllocation(self):
    MarkAllocation.delete(self)

def insertMarkAllocation(leaf_id_,assessment_id_,mark_,session_id_,marker_,student_,timeStamp_):
    temp = MarkAllocation(leaf_id=leaf_id_,mark=mark_,session_id=session_id_,marker=marker_,student=student_,timeStamp=timeStamp_)
    temp.save()
    return temp

def getMarkAllocation():
    temp=MarkAllocation.objects.all()
    return temp



class Aggregator:
    def aggregateMarks(self,assessment=[]):
        total = 0.0
        for x in range(len(assessment)):
            total += assessment[x]
        return total/len(assessment)
    def __unicode__(self):
        return "Aggregator"

class BestOfAggregator(Aggregator):
    numContributors = models.IntegerField()
    def aggregateMarks(self,assessment=[]):
        assessment.sort(reversed)
        total = 0.0
        for x in range(0,self.numContributors ):
            total += assessment[x]
        return (total/self.numContributors)
    def getnumContributors(self):
        return self.numContributors
    def setnumContributors(self,value):
        self.numContributors=value
        self.save()
    def __unicode__(self):
        return "BestOfAggregator"

def createBestOfAggregator(numContributors_):
    coA= BestOfAggregator(numContributors=numContributors_)
    coA.save()
    return coA



class WeightedSumAggregator(Aggregator):
    weight= []
    def aggregateMarks(self,assessment=[]):
        total = 0.0
        for x in assessment:
            total += assessment[x] * self.weights[x]
        return total/len(assessment)
    def __unicode__(self):
        return "WeightedSumAggregator"

def insertWeight(weightsstr_):
    weightsstrTemp = WeightedSumAggregator(weightsstr=weightsstr_)
    return weightsstrTemp

class SimpleSumAggregator(Aggregator):
    def aggregateMarks(self,assessment=[]):
        total = 0.0
        for x in range(len(assessment)):
            total += assessment[x]
        return total/len(assessment)
    def __unicode__(self):
        return "SimpleSumAggregator"




