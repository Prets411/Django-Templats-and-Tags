from django.shortcuts import render
from django.http import HttpResponse

def Mission(request):
    msg = "<h1>CCMS MISSION</h1> <h3>\nThe College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.</h3>"
    return HttpResponse(msg)

def Vision(request):
    msg = "<h1>CCMS VISION</h1> <h3>The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.</h3>"
    return HttpResponse(msg)

def Objectives(request):
    msg = "<h1>CCMS Objectives</h1> <h3>1. Increase faculty performance by obtaining a minimum rating of 4.00 in the semestral faculty evaluation of each faculty for the next fiveyears.</h3> \
        <h3>2. Maintain competent faculty line-up by sending all permanent fulltime faculty to at least one (1) IT related training, conference, orseminar annually for the next five years.</h3>\
            <h3>3. Conduct a minimum of two (2) researches, IT projects or production of instructional materials annually for the next five years.Achieve a minimum of 50 percent student passing percentage in the IT certification annually for the next five years.</h3>\
                <h3>4. Maintain state-of-the-art information technology learning environment through annual procurement or upgrading of hardwareor software licenses for at least one computer laboratory for the next five years.</h3>\
                    <h3>5. Set up minimum of two (2) academe-industry partnership projects and commercialization initiatives or research publication andpresentation annually in preparation for the next CHED COD/COE application.</h3>\
                        <h3>6. Strengthen promotion program to increase freshman enrollees to a minimum of three (3) class sections annually for the next five years.</h3>"
    return HttpResponse(msg)