* Anegdota o tym jak nazwałem prezentację "how to write faster code"
* Python nie jest najszybszym językiem
* .. but we don't care - we use Python because it's a great language and programming in Python is fun,
* give example of ugly code in Java and nice code in Python: stupid hello world will do:

    ```
    public class Main {
        public static void main(String[] args) {
            System.out.println("hello world");
           }
        }
        vs.
    print("Hello, world!")
    ```

* ... and for most of the use cases, it's just quick enough.
* Czasem jednak stwierdzamy że nasz kod jest zbyt wolny (we get timeouts on our website or maybe szybszy kod zwiększy zyski naszej firmy)
* So we decide to optimize our code
* How do you optimize your code ?
* Well, as with all programming questions, let's ask google!
* Google for 'optimization rule' (picture)
* We go a hit: http://c2.com/cgi/wiki?RulesOfOptimization
* Only 3 rules ? Great, so it has to be very simple !! Well, not really.
* Those rules looks like a joke, but actually they are very good rules.
* The first one: "Don't" - as I already said, 9 out of 10 times, you don't need the optimization.
* In case that you really need the optimization - rule number 2 "Don't do this yet". Many times when I was in the middle of working on some more or less complex code, I was thinking: "Hey, I can change this part of code and probably it will be faster - also I will save 2 lines of code". What was the outcome ? Sometimes, when I changed it, I broke something else. More often, I ended up jumping around the code and I forgot what I was writing in the first place. One way or another, it was causing confusion. Was the new code faster ? I don't know, since I didn't have anything to compare it to! If I had written the whole function first and then improve, I could measure the speed, but otherwise, I can only guess.
* That brings us to the third rule: "Profile before optimization". Human are terrible in predicting the bottlenecks of the code. If you think that a specific piece of your code is slow - profile it ! It might turn out that you would spend time rewriting some code just to make it 1% faster, while there are other parts of the code where you can gain huge improvements.