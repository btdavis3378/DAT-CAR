import owncloud

oc = owncloud.Client('http://192.168.1.66/owncloud')
oc.login('btdavis3378', 'rwv3ygeb')
oc.put_file('testdir/remotefile.txt', 'saved data.txt')
link_info = oc.share_file_with_link('testdir/remotefile.txt')
print ("Here is your link: " + link_info.get_link())
