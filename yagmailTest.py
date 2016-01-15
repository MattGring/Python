# Yagmail test
# be Me, 7/22/2015

# import statements
import yagmail

# instantiate an email object
# tried to use the keyring but the path to '.yagmail' could not be found
yag = yagmail.SMTP('gring.matt@gmail.com', '6shadow1')

# add some contents
# for more info: https://github.com/kootenpv/yagmail
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find a text file attached.', 'C:\\My Stuff\\2015-07-16.txt']

# send the message
yag.send('gring.matt@gmail.com', 'test subject', contents)
