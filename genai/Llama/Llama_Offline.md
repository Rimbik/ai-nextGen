# Run llama offline in your PC
    llma is a (meta/facebook) gpt model equivalent to chat gpt 3
---
#### What you are going to have with this ?
    *Overview: 
    Once you complete the process, you will be able to run lama model offline in your local PC. If you get success running all the steps mentioned here, you will be able to use a chatgpt kind of prompting system that runs in your local PC/Laptop.
    

    There are several llma models vailable in internet to download freely where some needs 2 GPU with 80GB RAM and some similar hardware but there is also low end models that llama were published with that can run on local PC having no GPU with only 4GB of RAM.



### Prerequistes:
    # a Linux PC/Laptop
    # decent RAM - minimum 4GB (as reported worked)
    # a decent CPU (rasberiPi with 4GB works)

    # basic c++ knowldge (not mandatory)
    # linux machine very basic skill to run commands and install several packages using sudo apt-get and pip

---

## Lets Start
This spec is influenced by a youtube link and all credit goes there. Therefire I would request you to first see the video to get some idea what is happening here. Link : 

Steps to folow sequentilly:
 - 1: Watch the youtube video to get the idea
 - 2: git clone the repo
 - 3: compile the project in Linux using make or cmake
 - 4: download the llama model that you want to run locally
 - 5: place the downloaded model in your cloned folder
 - 6: run few commands to make it running


----
Some References:
- llama model download path: 
        - https://www.llama.com/llama-downloads/

- additional file:
        - source code to clone :        
        - other files: https://github.com/cornelk/llama-go/blob/go/convert-pth-to-ggml.py

-----

Running Steps 1 by 1:

Step 1: Watch the video @ ''

Step 2: clone the llma.cpp project using the following command
    
     md llama
     cd llama
     git clone 
     ls

    now cd into the folder after complete cloning: (do not download from git, do clone only)

    james@james-bond:~/Other_Drive/AI_ML/gen_ai/LlaMa/lma/llama.cpp$

Step 3: Compile the project
        
    the video tutorial says use 'make' - make is a linux command that builds your project and in this case it is .cpp files. But you might facse challeges here and may be you run then 'cmake'. This part for any complecation we will discuss later but lets assume you are able to buld the project using make or cmake linux command

            - you mught need installing lots of linux packages as it will suggest if any compile error in the make or cmake command. So just follow the shell 

    [For many - it can be the hardest part to buidl the llama.cpp folder as it needs some C++ knowldge as how a c++ project compiles]. For me this steps became the hardest Step among all mentioned steps. So best of luck!

    "You are building a cpp (c++) project folder" in linux with source code opened.

    - If you are stuck for hrs with bad luck - move to step:4 (we still can do that later).     
      Consult me for any build issue in Linux.

Step 4: download the llama model from lama website (legal)

    https://www.llama.com/llama-downloads/
    
    [after vitiing the site, do the registration process as instructed]
    Fill the form and select your model to download.

    There are no of models and that are on top - they use heavy GPU that we do not have, so scroll down and find the "Previous language & safety models" to find the low end model that is "Llama 2" . This Llama-2 model we should be able to run locally in our local PC without any GPU.

    ![Lama 2 Model](images/llama2_model.png)
        

    Follow the instruction given in the web site to complete the download.

    Note: This is 13GB model and once done, it will be saved in your local PC '/home/' directory. For me it is '', also can be found in shell as you are downloading

    save/ytransfer the model to your desired folder in this case:
        
        A) go to your cloned folder
        B) paste in your model folder
    
    By now you are all set to start processing.







    












