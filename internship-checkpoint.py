{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4a425a83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram\n",
      "githa\n",
      "karan\n",
      "sonal\n"
     ]
    }
   ],
   "source": [
    "lst=[\"ram\",\"githa\",\"karan\",\"sonal\"]\n",
    "for i in lst:\n",
    "    print(i)\n",
    "\n",
    "     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a320ab1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4000, 299, 563, 734, 1568]\n",
      "[4000, 299, 563, 734, 1568]\n",
      "[4000, 299, 563, 734, 1568]\n",
      "[4000, 299, 563, 734, 1568]\n",
      "[4000, 299, 563, 734, 1568]\n"
     ]
    }
   ],
   "source": [
    "exp=[4000,299,563,734,1568]\n",
    "for i in exp:\n",
    "    print(exp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e1bbc1ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4001\n",
      "300\n",
      "564\n",
      "735\n",
      "1569\n"
     ]
    }
   ],
   "source": [
    "exp=[4000,299,563,734,1568]\n",
    "for i in exp:\n",
    "    print(i+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dcacec83",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1886600852.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[9], line 3\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(i--)\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "exp=[4000,299,563,734,1568]\n",
    "for i in exp:\n",
    "    print(i--)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7075310a",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate list (not \"int\") to list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[10], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m exp\u001b[38;5;241m=\u001b[39m[\u001b[38;5;241m4000\u001b[39m,\u001b[38;5;241m299\u001b[39m,\u001b[38;5;241m563\u001b[39m,\u001b[38;5;241m734\u001b[39m,\u001b[38;5;241m1568\u001b[39m]\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m exp:\n\u001b[1;32m----> 3\u001b[0m     \u001b[38;5;28mprint\u001b[39m(exp\u001b[38;5;241m+\u001b[39mi)\n",
      "\u001b[1;31mTypeError\u001b[0m: can only concatenate list (not \"int\") to list"
     ]
    }
   ],
   "source": [
    "exp=[4000,299,563,734,1568]\n",
    "for i in exp:\n",
    "    print(exp+i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2481db5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4000\n",
      "299\n",
      "563\n",
      "734\n",
      "1568\n"
     ]
    }
   ],
   "source": [
    "exp=[4000,299,563,734,1568]\n",
    "for i in exp:\n",
    "    print(++i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "88c77665",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum is 4000\n",
      "Sum is 4299\n",
      "Sum is 4862\n",
      "Sum is 5596\n",
      "Sum is 7164\n"
     ]
    }
   ],
   "source": [
    "exp=[4000,299,563,734,1568]\n",
    "total=0\n",
    "for i in exp:\n",
    "    total=total+i\n",
    "    print(\"Sum is\",total)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "33b89174",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected ':' (3448951672.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[13], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    for i in range(30, 51, 2)\u001b[0m\n\u001b[1;37m                             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected ':'\n"
     ]
    }
   ],
   "source": [
    "for i in range(30, 51, 2)\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e5b1d658",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "for i in range(30, 51, 2):\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c2aa418d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the value3\n",
      "3 X 1 = 3\n",
      "3 X 2 = 6\n",
      "3 X 3 = 9\n",
      "3 X 4 = 12\n",
      "3 X 5 = 15\n",
      "3 X 6 = 18\n",
      "3 X 7 = 21\n",
      "3 X 8 = 24\n",
      "3 X 9 = 27\n",
      "3 X 10 = 30\n",
      "3 X 10 = 30\n",
      "3 X 9 = 27\n",
      "3 X 8 = 24\n",
      "3 X 7 = 21\n",
      "3 X 6 = 18\n",
      "3 X 5 = 15\n",
      "3 X 4 = 12\n",
      "3 X 3 = 9\n",
      "3 X 2 = 6\n",
      "3 X 1 = 3\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter the value\"))\n",
    "for i in range(1,11):\n",
    "      print(a, \"X\", i,\"=\", a*i)\n",
    "for i in range(10,0,-1):\n",
    "    print(a,\"X\",i,\"=\",a*i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "242a0d1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "8\n",
      "12\n",
      "16\n",
      "20\n",
      "24\n",
      "28\n",
      "32\n",
      "36\n",
      "40\n"
     ]
    }
   ],
   "source": [
    "for i in range(4, 41, 4):\n",
    "   print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "dbb397b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "8\n",
      "12\n",
      "16\n",
      "20\n",
      "24\n",
      "28\n",
      "32\n",
      "36\n",
      "40\n"
     ]
    }
   ],
   "source": [
    "for i in range(4, 41, 4):\n",
    " print(i)\n",
    "for j in range(40, 5, 4):\n",
    "    print(j)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a1a782e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number4\n",
      "4\n",
      "8\n",
      "12\n",
      "16\n",
      "20\n",
      "24\n",
      "28\n",
      "32\n",
      "36\n",
      "40\n"
     ]
    }
   ],
   "source": [
    "a= int(input(\"Enter a number\"))\n",
    "for i in range(4,41,4):\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2bb29cd4",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'for' statement on line 5 (231194545.py, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[29], line 6\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(i)\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after 'for' statement on line 5\n"
     ]
    }
   ],
   "source": [
    "des=int(input(\"Enter the destination floor\"))\n",
    "total=10\n",
    "current=3\n",
    "if(destination>current):\n",
    "    for i in range(3,11,2):\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a527100b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
