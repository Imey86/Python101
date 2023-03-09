class School:
    #Attribute
    schoolName = 'ลุงวิศวกร สอนคำนวณ'

    # Constructor
    def __init__(self,subject):
        print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        self.subject = subject
    
    # Method
    def hello(self):
        print('สวัสดีตอนเช้า ยินดีต้อนรับนักเรียนทุกคน')

    def teach(self):
        print(f'โรงเรียนนี้ เปิดสอนวิชา {self.subject}')

# Instance
school1 = School('Python Programming')
print(f'ชื่อโรงเรียน : {school1.schoolName}')
school1.hello()
school1.teach()
