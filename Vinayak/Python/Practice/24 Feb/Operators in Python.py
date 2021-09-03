#Python Operators
#Arithmetic Operators
+ 	Addition 	    x + y    5+3   8
- 	Subtraction 	x - y 	 5-3   2
* 	Multiplication 	x * y 	 5*3   15
/ 	Division 	    x / y 	 5/3   1.666667
% 	Modulus 	    x % y 	 5%3   2
** 	Exponentiation 	x ** y 	 5**3  5*5*5
// 	Floor division 	x // y   5//3  2

#Assignment Operators
=      x = 5 	x = 5 	     
+= 	   x += 3 	x = x + 3 	 5+3   8
-= 	   x -= 3 	x = x - 3    5-3   2	
*= 	   x *= 3 	x = x * 3 	 5*3   15
/= 	   x /= 3 	x = x / 3 	 5/3   1.66666667
%= 	   x %= 3 	x = x % 3 	 5%3   2
//=    x //= 3 	x = x // 3 	 5//3  1
**=    x **= 3 	x = x ** 3 	 5**3  125
&= 	   x &= 3 	x = x & 3 	 5&3   1
|= 	   x |= 3 	x = x | 3 	 5|3   7
^= 	   x ^= 3 	x = x ^ 3 	 5^3   6
>>=    x >>= 3 	x = x >> 3 	 5>>3  0
<<=    x <<= 3 	x = x << 3   5<<3  40

#Python Comparision Operators
== 	Equal 	                 x == y   5===3   False 	
!= 	Not equal                x != y   5!=3    True
> 	Greater than             x > y 	  5 > 3   True
< 	Less than 	             x < y 	  5 < 3   False
>= 	Greater than or equal to x >= y   5>=3    True
<= 	Less than or equal to 	 x <= y   5<=3    False

#Python Logical Operators
and    Returns True if both statements are true 	                x < 5 and  x < 10 	
or 	   Returns True if one of the statements is true 	            x < 5 or x < 4 	
not    Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)

#Python Identity Operators
is  	Returns True if both variables are the same object 	x is y 	
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

is not 	Returns True if both variables are not the same object 	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Python Membership Operators
in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


