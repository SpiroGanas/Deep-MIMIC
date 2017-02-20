# Setting up a virtual machine

These are the steps I followed to set up TensorFlow on a virtual machine running on the Amazon Cloud


## Launching a Virtual Machine on the Amazon Cloud
1.  Log in to the Amazon Cloud console and go the the EC2 Dashboard
2.  Click the "Launch Instance" button.  Select the Ubuntu Server 16.04 LTS image.
3.  Select the hardware you want to use.  A "medium" type should work for now.
4.  On the "Add Storage" screen, add a 300 Gigabyte "EBS" hard drive.
5.  Launch the instance and use SSH to connect to it.



## Formatting the attached storage
1.  Find out the name of the "EBS" hard drive.  http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
    ```shell
    lsblk 
    ```

2.  Create a file system on the sike
    ````shell
    sudo mkfs -t ext4 /dev/xvdb
    ````

3.  Mount the file system
    ````shell
    sudo mkdir /data
    sudo mount /dev/xvdb /data
    ````

4.  Change the owner of the drive from root to the user ubuntu
    ````shell 
    sudo chown -R ubuntu:ubuntu /data
    ````


The hard drive will now be see by typing
    ````shell
    cd /data
    ````




## Installing TensorFlow
1.  Update all the package.
    ```Shell
     sudo apt-get update
    ```
    If you get an "unable to resolve host",  "This can be solved by allowing DNS hostnames at the VPC level. Go the the VPC management console, select the VPC, click on Actions, select Edit DNS Hostnames and select Yes." https://forums.aws.amazon.com/message.jspa?messageID=495274 



2.  Python version 3 should already be installed, but you will need to install the pip package manager.
    ```Shell
    sudo apt-get install pip3
    ```
3.  Once pip3 is installed, make sure it's the latest version by using it to update itself.
    ```Shell
    pip3 install --upgrade pip
    ```

4.  You will also need to make sure you have the Python development files.
    ```Shell
    sudo apt-get install python3-dev
    ```
5.  Then you can install TensorFlow using pip.
    ```Shell
    pip3 install tensorflow
    ```

6.  Test Tensorflow using using the method on the TensorFlow website:  https://www.tensorflow.org/install/install_linux#ValidateYourInstallation

    First run Python from the shell:
    ```Shell
    python3
    ```

    Then write a vry small TensorFlow program:
    ```python
    import tensorflow as tf
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))
    ```


## Installing the MIMIC-III database
1.  Request access to the MIMIC-III data.  https://mimic.physionet.org/gettingstarted/access/

2.  Create a folder to store the data.
    ```Shell
    mkdir MIMIC_Data
    cd MIMIC_Data
    ```

3.  Use wget to download all the zipped data files.
    ```Shell
    wget --user YOURUSERNAME --ask-password -A csv.gz -m -p -E -k -K -np -nd https://physionet.org/works/MIMICIIIClinicalDatabase/files/
    ```

4.  unzip all the data files.
    ```Shell
    gunzip -r .
    ```

You will now have one .csv file for each table listed in the MIMIC-III data dictionary:  https://mimic.physionet.org/mimictables/admissions/

 


## Install Juptyer Notebooks
1.  Install Jupyter notebooks, the new version of "IPython Notebooks" 
    ```shell
    sudo pip3 install jupyter
    ```
    
2.  On the Amazon Cloud "Security Group" page, add a firewall rule to allow the server to respond to incomming TCP traffic on port 8888.

3.  Follow these instructions to set up jupyter notebooks: http://chrisalbon.com/jupyter/run_project_jupyter_on_amazon_ec2.html

Make sure you remember the password, you will need it to log on the the website.
     
4.  Launch the Jupyter notebooks server.
    ```shell
    jupyter notebook
    ```

5.  Use a web browser on your local computer to connect to https://TheAmazonServerName:8888













