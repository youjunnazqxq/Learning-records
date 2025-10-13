## Q1

```
(define (vir_fib n)

 (if (<= n 1)

        1

        (+(vir_fib(- n 1) (vir_fib_(- n 2)))

 )

)
```



## Q2

```
(define with-cons (cons (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil))) ) )
```


## Q3


```
(define (list-concat a b)

 (if (null? a)

    b

    (cons (car a)(list-concat(cdr a) b))

 )

  

)
```


## Q4

```
(

    define (remove item lst)

    (

        cond ((null? lst) ())

        ((equal? item (car lst)) (remove item (cdr lst)))

        (else (cons(car list) (remove item (cdr lst))))

    )

)
```