## Introduction
* Anegdota o tym że jak nazwałem prezentację "How to write faster code", ktoś zwrocił mi uwagę, "Rewrite your code in C" - i wiecie co ? ten gość miał rację. Dlatego chciałem zmienić tytuł na "How to write faster code and don't hate your job as a software developer", żeby nikt się nie pomylił z pisaniem kodu w C, ale w końcu stwierdziłem że wystarczy "Writing faster Python".
* Wszyscy dobrze wiemy, że Python nie jest wybierany ze względu na jego szybkość. And it's fine, in most of the cases, Python's speed is just fine.

## What to do when your code is slow ?
* Czasem jednak przychodzi czas, że stwierdzamy, że nasz kod jest zbyt wolny - nadchodzi czas na optymalizację.
* * Let's see what happens when you know what you want to optimize.
* The first thing you do, you probably google for something like 'optimization rule' and you click the first website you find: http://c2.com/cgi/wiki?RulesOfOptimization. Huh? Only 3 rules? That should be simple. Well, not really.
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
    + Rewriting your code in C or C++. You can write a module in C that you can then use in your code.
    + You could change the Python compiler to a different one (PyPy instead of CPython?)
* However, quite often you can improve you code by changing your algorithm. Is most of the time spend waiting for I/O ? Then maybe it's time to use asynchronous library instead.
* Even when you already have a good algorithm, you can further refine it by using correct data structures or avoiding some anti-patterns.

* One important thing to note here is that there are various levels of optimization (https://en.wikipedia.org/wiki/Program_optimization):
    - Design level - it's the highest level of optimization. Depending on the constrains and priorities of your system, you can optimize it by redesigning it. It might require rewriting your parts or the whole application in a different programming language that might be faster, changing the type of database you are using so it fits your needs betters or redesigning the architecture of your software to limit the number of DB queries etc. We are probably not interested in that today, as we are not going to rewrite something that we have been working very hard on in the past months/years. However, if you have some critical parts of the code that is run often, you can optimize it by rewriting it in C or C++.The advantage is that C is faster, so you will get some speed improvement for free. Well, not really for free - now you have to maintain Python AND C/C++ code.
    - Algorithms and data structures - one level lower, we have algorithms. That's usually the second biggest improvement you can get after after a complete redesign. Knowing different algorithms together with their complexity definitely helps. For example, you want to get a sum of numbers from 1 to N. The first idea might be a loop:
    ```
    sum = 0
    for x in range(1, N+1):
        sum += x
    print sum
    ```
    which will work, but you can also use an algorithm for the arithmetic sum:
    ```
    print N * (1 + N) / 2
    ```
    which will give the same results AND it will be more efficient.
    - Source code - this is something that I will be talking about today.
    - Build level - Low level optimization, that involves setting up specific build flags. In your daily work, it's not something that you do often. You can optimize the Python build for a specific architecture, but if you are a web developer like me, most of the time you don't go to this level of optimization.
    - Compile level - you can make some optimization if you are using Ahead of Time compiler. Which is not the case for Python, as there is not ahead of time compiler for Python.
    - Assembly level - this is probably as low as we can get. For additional performance, you can write directly the assembly code for a specific architecture. As this is "Python Developers Forum", not "Assembly Developer Forum", I will not focus on this level of optimization either.
    - Run time - it's related with the specific compiler you are using. Some compilers are faster than the other, for example, if you replace CPython with PyPy, you can gain up to 7x speed improvement (http://speed.pypy.org/), but again, it depends of what task you are doing. Most of the time once we set up on a specific language implementation, there is nothing we have to do to benefit from this kind of optimization - it's up to the creators of the compilers to optimize them, so simply updating to new version of the programming language you are using can make your programs run a bit faster.
* Another important thing that we need to remember here - optimization is not only about the speed. Sometimes, optimization can have nothing to do with the execution time at all, as there can be other resources more important than raw speed. You can optimize memory usage, disk space usage, disk IO, bandwidth, power consumption and other resources.
    + Sometimes maybe the memory consumption will be more important than the speed of a script. Who cares that your program is now 10 times faster if it now crashes half of the time because of too big memory consumption ?
    + Quite often, optimization in one area will cause deterioration in the other. Let's say that you have some computations that require processing a lot of data. You might run out of RAM if you store all of it in the memory, so you can store intermediate results on the disk. This will make you program consume less memory, but it will be slower due to more disk IO, so you have to decide which of those resources is more important to you.
* Also, unless your code is "write and forget" (which probably isn't, so please be nice to people who will be maintaining it! - tweet about _always write code as the person who will maintain it is a psychopath who knows where you live_), if you are making the code harder to read and maintain, then you are probably doing it wrong.

## Why do I care about source code optimizations ?
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

## Summary
* Different kinds of optimizations (it's not always about the speed)
* Different levels of optimization (some of them are harder to do, but will give you more benefits)
* Although major optimizations should be done (if ever) after you have the working software, source code optimizations can be applied when you write the code and they have little to none trade-offs:
    - Don't reinvent the wheel, use functions from the standard library
    - Idiomatic Python code is usually faster
* Profile and be curious !