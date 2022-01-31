### GUILLAUME THIVOLET TASK3

<div style="text-align: justify">
In its state my code for task3 does not compile.

I was initially aiming for [BLUE Prefetcher](https://webs.um.es/aros/papers/pdfs/aros-mldpc21.pdf), which was presented in the 2021 ML-Data prefetcher competition but got stuck on a few implementation details after reading the paper during the semester. It is a combination of [Berti prefetcher](https://webs.um.es/aros/papers/pdfs/aros-dpc19.pdf), [Entangling]() and a next line prefetcher with a degree of 2.

BLUE is a prefetcher based on timeliness, which is not a metric accessible within Champsim (see [Section 7](https://webs.um.es/aros/papers/pdfs/aros-dpc19.pdf)).

Thus is it not possible to implement correctly BLUE.

I decided to give it another try during the examination session, but this time focusing on the Berti prefetcher only and not BLUE which was a derivate of Berti.

I still didn't manage to complete my implementation. It is missing the previous demand requests and previous prefetches tables from the paper, which prevents me to compute the berti delta (stride) and to issue the prefetches. I still left my non-achieved work in the submission.

In retrospective, I would have chosen a different prefetcher to implement.

</div>
