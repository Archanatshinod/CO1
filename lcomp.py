{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOqnUW/7WBnW5IeygQ2OvRI"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":5,"metadata":{"id":"9-ZSD4ICk0Kw","colab":{"base_uri":"https://localhost:8080/"},"outputId":"271e3cff-5cf4-482d-8544-89e6cb02126b","executionInfo":{"status":"ok","timestamp":1669646124389,"user_tz":-330,"elapsed":28262,"user":{"displayName":"ARCHANA T","userId":"18273571569451510332"}}},"outputs":[{"output_type":"stream","name":"stdout","text":["list [1, -4, 500, 13, 7, -10]\n","postive numbers from given list\n","[1, 500, 13, 7]\n","enter the number of elements:3\n","enter the number 2\n","enter the number 3\n","enter the number 4\n","sqaure of numbers\n","[4, 9, 16]\n","enter a string:english\n","['e', 'i']\n","the ordinal values\n","[101, 110, 103, 108, 105, 115, 104]\n"]}],"source":["num=[1,-4,500,13,7,-10]\n","print(\"list\",num)\n","new_lst=[x for x in num if x>0]\n","print(\"postive numbers from given list\")\n","print(new_lst)\n","lst=[]\n","n=int(input(\"enter the number of elements:\"))\n","for i in range(0,n):\n","    a=int(input(\"enter the number \"))\n","    lst.append(a)\n","list1=[i*i for i in lst ]\n","print(\"sqaure of numbers\")\n","print(list1)\n","vowel=['a','e','i','o','u']\n","name=input(\"enter a string:\")\n","new_str=[x for x in name if x in vowel]\n","print(new_str)\n","ord_lst=[ord(x) for x in name]\n","print(\"the ordinal values\")\n","print(ord_lst)"]}]}