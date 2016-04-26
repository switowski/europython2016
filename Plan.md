## Introduction
* Anegdota o tym że jak nazwałem prezentację "How to write faster code", ktoś zwrocił mi uwagę, "Rewrite your code in C" - i wiecie co ? ten gość miał rację. Dlatego chciałem zmienić tytuł na "How to write faster code and don't hate your job as a software developer", żeby nikt się nie pomylił z pisaniem kodu w C, ale w końcu stwierdziłem że wystarczy "Writing faster Python".
* Wszyscy dobrze wiemy, że Python nie jest wybierany ze względu na jego szybkość. And it's fine, in most of the cases, Python's speed is just fine.

## What to do when your code is slow ?

* Czasem jednak przychodzi czas, że stwierdzamy, że nasz kod jest zbyt wolny - nadchodzi czas na optymalizację. When this time come, the first thing you do, you probably google for something like 'optimization rule' and you click the first website you find: http://c2.com/cgi/wiki?RulesOfOptimization. Huh? Only 3 rules? That should be simple. Well, not really.
* Rule number 1: Don't. Ok, that was not very helpful.
* Rule number 2: Don't yet. This is a very good advice. How I understand it is:
    + First write the code that is passing your tests - don't bother if it's ugly or slow - make sure it works.
    + Then, you clean your code and optimize (it if really needed)
* I really like this rule. Many times when I was in the middle of working on some more or less complex code, I was thinking: "Hey, I can change this part of code and probably it will be faster - also I will save 2 lines of code". What was the outcome ? Sometimes, when I changed it, I broke something else. More often, I ended up jumping around the code and I forgot what I was writing in the first place. One way or another, it was causing confusion. Was the new code faster ? I don't know, since I didn't have anything to compare it to! If I had written the whole function first and then improve, I could measure the speed, but otherwise, I can only guess.
* That brings us to the third rule: "Profile before optimization". Human are terrible in predicting the bottlenecks of the code. If you think that a specific piece of your code is slow - profile it ! It might turn out that you would spend time rewriting some code just to make it 1% faster, while there are other parts of the code where you can gain huge improvements.

## Profiling tools

* There are many great tools out there, that you can use to profile your code. One of the most common is the CProfile - which is part of Python standard library.
* **Show how to use CProfile**
* There are also some other profiling tools, for example graphical ones like "run snake run", etc.
* Ok, so you have found the slow part of your code, what next ?
* There are few solutions that you could use, some of them are more drastic, like:
    + Rewriting your code in C or C++. You can write a module in C that you can then use in your code. The advantage is that C is faster, so you will get some speed improvement for free. Well, not really for free - now you have to maintain Python AND C/C++ code.
    + You could change the Python compiler to a different one (PyPy instead of CPython?)
* However, quite often you can improve you code by changing your algorithm. Is most of the time spend waiting for I/O ? Then maybe it's time to use asynchronous library instead.
* Even when you already have a good algorithm, you can further refine it by using correct data structures or avoiding some anti-patterns.

## Why do I care about this micro-improvements ?
* I don't know about you, but when I'm coding, for each line of code I'm always wondering if this is the best way to write my code. Maybe if instead of a loop I can use map ? Will it be faster ? Should I cache this variable or not ?
* This is one of the reasons why I love Python - one of it's rules/dogmas are "There should be only way to do it".
* For example, take a look at this function:
* **Example of a slow function and a faster version**
* When you profile it, you can see that even though it's like 1000x times faster, it's still just 1 ms faster. However, if the part of code where you just saved 1 ms is executed 1 million times, then this improvement matters.
* **Optional???** Ok, but who is executing code 1 million times ? For example, physicists. I'm working at CERN, where the main users are physicists from around the world. Most of them don't have any computer science background, yet they write scripts all the time (because of it's easy of use, Python is very popular among physicists). Those scripts are analyzing terrabytes of data (just for the scale, LHC is producing around 25GB of data per second), so even 1 ns saved in a loop is a huge improvement.
* So let's take a look as some examples and how we can make them faster.

## Examples:
* To compare the execution time of different code snippets, I'm using the magic function %timeit of the IPython. It's a really cool one liner that basically wraps the timeit function from Python's standard library. It has some overhead comparing to using the `timeit` directly, but we don't care since we use the same technique to profile code snippets, so we can neglect the overhead.
* Let's start with something simple: let say we want to count the elements in the list. You can easily write a simple loop than increments a counter and there is nothing wrong with this code, except that it's slow. You can achieve the same results using the built-in function len(). And as you can see the speed improvement is quite huge.
* Write idiomatic Python


## Important things to remember (move it up)
* Speed is not everything - you have to remember about other important factors, when you optimize.
    + Sometimes maybe the memory consumption will be more important than the speed of a script. Who cares that your program is now 10 times faster if it now crashes half of the time because of too big memory consumption
    + Also, unless your code is "write and forget", if you are making the code harder to read and maintain, then your doing it wrong (always code as if the person maintaining your code is a psychopath who knows your address)
