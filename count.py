{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPwM2n3zt9/F80nPMopPFbU"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":401},"id":"HJVEHDQ-P3Gl","executionInfo":{"status":"error","timestamp":1671366082336,"user_tz":-330,"elapsed":16653,"user":{"displayName":"ARCHANA T","userId":"18273571569451510332"}},"outputId":"9b8034e8-5df2-4283-f777-d8406031a079"},"outputs":[{"name":"stdout","output_type":"stream","text":["Enter text:red blue green red\n"]},{"output_type":"error","ename":"NameError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)","\u001b[0;32m<ipython-input-1-37375eea998d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstr1\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\" \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m       \u001b[0;32mif\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mword\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m             \u001b[0mcount\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcount\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m       \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Count of the word is:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mNameError\u001b[0m: name 'word' is not defined"]}],"source":["str1=input(\"Enter text:\")\n","a=[]\n","count=0\n","a=str1.split(\" \")\n","for i in range(0,len(a)):\n","      if(i):\n","            count=count+1\n","      print(\"Count of the word is:\")\n","      print(count)"]}]}