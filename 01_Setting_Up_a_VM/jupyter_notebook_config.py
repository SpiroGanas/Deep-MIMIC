# This is a sample jupyter configuration file
# The file need to be copied to the folder:  ~/.jupyter/
#
# in this example, the password is: helloworld
#
# You can create a custom password by following the instructions at: http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html



c = get_config()


# if you want plotting support always in your notebook
c.IPKernelApp.pylab = 'inline'  

# Notebook config

#location of your certificate file
c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem' 

c.NotebookApp.ip = '*'

#so that the ipython notebook does not opens up a browser by default
c.NotebookApp.open_browser = False  



#the encrypted password we generated above
c.NotebookApp.password = u'sha1:fd591b839377:4c6dc6bbc958d918838bfd6a2cece1db8841bfdf'


  
# It is a good idea to put it on a known, fixed port
# In the Amazon Cloud Security Group dashboard, we need 
# to allow incoming TCP traffic on this port
c.NotebookApp.port = 8888