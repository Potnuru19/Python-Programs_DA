'''
Assignment - 1
Using List, Set, Dictionary --> designed a program on codegnan portal.

'''

#list --> stores multiple values

daily_exams = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
subjects = ['Python','Aptitude','Softskills','MYSQL','POWER BI']
mock_interviews = ['Technical','HR','Communication']
project_demos = ['ATM Project','MYSQL Student Database Management System Project','Data Analytics Project']


#set --> stores unique streak values
attendance_streak = {1,2,3,4,5,6,7,8,9,10}
mock_interview_streak = {1,2,3,4,5}


#dictionary --> connects each portal feature with its details
codegnan_portal = {
    'Daily Exams': daily_exams,
    'Subjects': subjects,
    'Mock Interviews': mock_interviews,
    'Project Demos': project_demos,
    'Attendance Streak': attendance_streak,
    'Mock Interview Streak': mock_interview_streak
}
#display details
print("-----------CODEGNAN PORTAL-----------")
print('Daily Exams:',codegnan_portal['Daily Exams'])    
print('Subjects:',codegnan_portal['Subjects'])    
print('Mock Interviews:',codegnan_portal['Mock Interviews'])    
print('Project Demos:',codegnan_portal['Project Demos'])    
print('Attendance Streak:',codegnan_portal['Attendance Streak'])    
print('Mock Interview Streak:',codegnan_portal['Mock Interview Streak'])    
