"# Is Prime
Define a function `isPrime` that takes one integer argument and returns `true` or `false` depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Example
```ruby
isPrime(5)
=> true
```

## Assumptions
* You can assume you will be given an integer input.
* You can not assume that the integer will be only positive. You may be given negative numbers.

<div style=\"border:1px solid #a00;padding-left:8em;position:relative;\"><span style=\"background:#a00;display:inline-box;padding:0.5em 0.5em;position:absolute;left:0;top:0;bottom:0;vertical-align:middle;font-size:2em;font-variant:small-caps\">Bug!</span><p>The Haskell version uses a wrong test case, where negative primes should also return `True`, e.g. it expects <code>isPrime&nbsp;(-2)&nbsp;==&nbsp;True</code>. Use `abs` or similar measures to take care of negative numbers. The test cases cannot get changed at this point. Sorry for the inconvenience.</p>
</div>"