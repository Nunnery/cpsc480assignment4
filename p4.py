from operator import attrgetter
from csv import reader


class CnuClass(object):
    def __init__(self, crn, course, section, title, hours, aoi, type, days, time, location, instructor, seats, status):
        self.crn = crn
        self.course = course
        self.section = section
        self.title = title
        self.hours = hours
        self.aoi = aoi
        self.type = type
        self.days = days
        self.time = time
        self.location = location
        self.instructor = instructor
        self.seats = seats
        self.status = status

    def __repr__(self):
        return (('<CnuClass crn:"{self.crn}" course:"{self.course}" section:"{self.section}" title:"{self.title}" ' +
                 'hours:"{self.hours}" aoi:"{self.aoi}" type:"{self.type}" days:"{self.days}" time:"{self.time}" ' +
                 'location:"{self.location}" instructor:"{self.instructor}" seats:"{self.seats}"' +
                 'status:"{self.status}">').format(self=self))


# Define a switch class because switches are so much nicer than
# if-else-if-else-if-else-if-else-if-else-if-else blocks.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


def load_cnu_classes():
    # Initialize the classes list
    cnu_classes = []
    with open('ScheduleOfClasses.csv') as f:
        for line in reader(f):
            cnu_classes.append(CnuClass(line[0], line[1], line[2], line[3],
                                        line[4], line[5], line[6], line[7],
                                        line[8], line[9], line[10], line[11],
                                        line[12]))
    return cnu_classes


def print_help():
    print '\nEnter one of the following commands:'
    print '\tPRINT: Prints all of the available classes in the system.'
    print '\tEXIT: Exits the program.'
    print '\tAOI [aoi]: If argument is given, finds all classes with given AOI. Otherwise, sorts by AOI.'
    print '\tCOURSE [course]: If argument is given, finds all classes with given course. Otherwise, sorts by course.'
    print '\tCRN [crn]: If argument is given, finds all classes with given CRN. Otherwise, sorts by CRN.'
    print '\tDAYS [DAYS]: If argument is given, finds all classes with given days. Otherwise, sorts by days.'
    print '\tHOURS [hours]: If argument is given, finds all classes with given hours. Otherwise, sorts by hours.'
    print '\tINSTRUCTOR [INSTRUCTOR]: If argument is given, finds all classes with given location. Otherwise,' + \
          ' sorts by location.'
    print '\tLOCATION [LOCATION]: If argument is given, finds all classes with given location. Otherwise, sorts' + \
          ' by location.'
    print '\tSEATS [SEATS]: If argument is given, finds all classes with given seats. Otherwise, sorts by seats.'
    print '\tSECTION [section]: If argument is given, finds all classes with given section. Otherwise, sorts by' + \
          ' section.'
    print '\tSTATUS [STATUS]: If argument is given, finds all classes with given status. Otherwise, sorts by status.'
    print '\tTIME [TIME]: If argument is given, finds all classes with given time. Otherwise, sorts by times.'
    print '\tTITLE [title]: If argument is given, finds all classes with given title. Otherwise, sorts by title.'
    print '\tTYPE [TYPE]: If argument is given, finds all classes with given type. Otherwise, sorts by type.'


known_classes = load_cnu_classes()
running = True
print 'Welcome to the CNU Schedule Query System (CNUSQS)!'
while running:
    print_help()
    command = raw_input('\n\nEnter a command: ')
    split_command = command.split(' ')
    for case in switch(split_command[0].upper()):
        if case('PRINT'):
            print "\n".join(map(str, known_classes))
            break
        if case('EXIT'):
            running = False
            break
        if case('AOI'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.aoi.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('aoi'))))
            break
        if case('COURSE'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.course.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('course'))))
            break
        if case('CRN'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.crn.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('crn'))))
            break
        if case('DAYS'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.days.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('days'))))
            break
        if case('HOURS'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.hours.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('hours'))))
            break
        if case('INSTRUCTOR'):
            if len(split_command) > 1:
                print "\n".join(map(str, [x for x in known_classes \
                                          if x.instructor.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('instructor'))))
            break
        if case('LOCATION'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.location.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('location'))))
            break
        if case('SEATS'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.seats.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('seats'))))
            break
        if case('SECTION'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.section.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('section'))))
            break
        if case('STATUS'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.status.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('status'))))
            break
        if case('TIME'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.time.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('time'))))
            break
        if case('TITLE'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.title.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('title'))))
            break
        if case('TYPE'):
            if len(split_command) > 1:
                print "\n".join(
                    map(str, [x for x in known_classes if x.type.upper() == ' '.join(split_command[1:]).upper()]))
            else:
                print "\n".join(map(str, sorted(known_classes, key=attrgetter('type'))))
            break
        if case():
            print 'Please use a valid command!'
    if running == True:
        placeholder = raw_input('PRESS ENTER TO CONTINUE')
