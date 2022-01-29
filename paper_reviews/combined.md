==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

1

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

3

==+== C. Paper summary

This is a talk from Richard Hamming at a Bells Labs seminar. Richard shares observations he witnessed across his years at Bells Labs, and specifically teaches the audience what is the difference between doing nobel-worthy class work and regular great work.

It is a mix of field-tested advices and remarks that go a long way to motivate us in our daily research to reach this level. A good scientist doesn't only excel in pure technicality, but is also ears-open, a proliferous literate fellow that strives to keep improving. Struggling is part of the journey, and in the long run what makes the reward so satisfying. He also mentions the importance of being in a collaborative fruitful environment and to not fight but rather embrace it for highest impact.

Ultimately one should know why he is involved in research, but for truly nobel-class and revolutionizing work, passion is also a deciding factor. At the cost of sometimes neglecting other aspects of your life, but dedicating your life for the greater good. Thriving for the highest-quality is not achieved by being born a genius nor luck, but rather by constant small improvements and dedication that triggers your inner both.

To conclude, this is a motivational speech that illustrates the payoffs that can be reached for being clear about your ambitions and not only pursuing a dream, but working towards turning it into reality.

==+== D. Comments for author

This is a speech that I very much agree with, and will definitely come back to read once or twice in year. It is very difficult for someone to ask the question: Is the research that I am working on worth it?, because it boils down to your own interest and there's no point in working on something that doesn't excite you.

Best research is not performed when young: best research is performed when an individual as the strongest drive and the feeling that *anything* can be achieved with a strong willpower. That along with not being yet impacted by life hazards, administrative snags, or whatever is what makes us feel that the best research is performed when young.  

Burnout of overpressure imposed by a manager, lab head, is however very real. Movies like Whiplash (2014) illustrate this in an elegant manner. Fleeing a toxic environment should not be frowned upon, as disregarding uninterested or disregarding colleagues should not be seen negatively. It is up to you to create your best environment but to also understand that what you perceive as the best, less stressful can not be the most ideal conditions to reach better than great work.

Steering your own research towards your field's biggest interests, or at least not closing doors is however of the upmost importance. Not doing this could result in lack of funding, being disregarded by your peers, not listened to (John Turkey's example) when *sometimes* a slight show of interest or simple questioning can lead to magnitude higher impacts. Hence the need to foresee your field's bottlenecks.

Some quotation from the speech that I was very found of:
- It is a poor workman who blames his tools - the good man gets on with the job, given what he's got, and gets the best answer he can
- Embrace your environnement, however it impacts you, and get the best out of it
- don't be a back room scientist
- If what you are doing is not important, and if you don't thin that it leads to something important, then why are you at Bells Labs working on it?

# Strength

- Highly motivational!
- Enumerations of conditions for an individual to be productive
- Illustrations with lots of examples
- Teaches us to work with our tools, not against them
- Factors in luck, and genius are not born nobel

# Weaknesses

- Hard work always pays off but is also often synonym of burning out if never rewarded
- Lots of self-bias due to an extremely fruitful environment
- How to push less brilliant scientists to become great scientists?
- Should all of the work be for nobel-class? Can it?

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

It is a poor workman who blames his tools - the good man gets on with $
the job, given what he's got, and gets the best answer he can

 The struggle to make something of yourself seems to be 
worthwhile in itself

Embrace your environement, however it impacts you, and get the best out of it

know your weaknesses, the strength

conforisming can go a long way
difference between good work and first class work

dont be a back room scientist

stad on the shoulders of giants
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

10

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

1

==+== C. Paper summary

The paper present  two new methods for hash codings, which are evaluated according to three factors: the hash size area size, the access time and the allowable fraction of errors. In a more classical hash function, there are no possibilities of getting an error. The methods permit for some error rate in the hashing with false positives, but no false negatives. The gain is a greatly diminished impact on the storage space which allows for bigger sets to have their hash area realistically storable. An example is shown for an automatic hyphenation of a large dictionary, that the author compared to traditional methods, saving 88.5% of space with a 1/64 accepted error rate.

==+== D. Comments for author

# Strengths

+ Normalized space/time tradeoff measurement (removed set size dependency for analysis)
+ Thorough analysis of the three methods
+ Novelty of the presented method

# Weaknesses

+ The analysis assumes a bit-by-bit access, which is never the case
+ Notations are not consistent / well chosen across the paper (b,c,h,\phi,d,N,x)
+ The method 1 seems to serve only as a benchmarking to prove the second method's efficiency.
+ Missing a conclusion

The paper is well redacted and easy to follow. The method presented drastically reduces the necessary has storage size, which could be a bottleneck in the future. The analysis of the performance improvement assumed a precise pattern for hashing match verification (ie. bit-by-bit, sequential verification), which is a huge hypothesis shortcut. Nevertheless, the method and the analysis presented are enough to understand and prove its efficiency. It could have been interesting to show other use cases although the one picked was relevant.

In conclusion, an opening on future improvements could have proved useful for the interested reader.

-Table 1, a reminder of the initial hash size area for the traditional method could have been included to ease the reading
-A figure to illustrate method 2 would have been convenient

==+== E. Comments for PC

There is great value for future application in the now so-called Bloom filter, which will remain useful whatever the memory access scheme. This paper deserves to be accepted.

==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

13

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Ambit proposes augmented DRAM functionalities with access to new bulk-bitwise operations in 3 rows at a time inside a DRAM (NOT, OR, AND operation). Ambit is compatible with existing DRAM commands and address interface. Its solution is low-cost and entails only a 1% overhead in the existing technologies.

It does so by modifying slightly DRAM cells and the sense amplifier. Ambit AND-OR uses Triple row-activations (TRA) which connect a sense amplifier with three DRAM cells on the same bitline, while Ambit-NOT relies on the introduced Dual-contact cell (DCC). The DCC has two transistors wired on the sense-amplifier bitline and ~bitline, allowing for an efficient negation of the data by the Ambit controller.

Ambit divides the addresses array in the DRAM in three categories (Bitwise, Control and Data). In its current implementation, each sub-array contains 2 C-group, 8 B-group addresses while the D ones retain data.

Those reserved addresses are required to perform the AMBIT-operations with the TRA and DCC cells logic. The row decoder is split into two to simultaneously decode B-group and C/D-group addresses, to speedup the execution of the new Activate-Activate-Precharge primitive sequence.

Extensive hardware cost evaluation has been performed to push its industrial use.

The performance improvement of Ambit is best when compared to the targeted cloud applications (database bitmap indices,BitWeaving and bit-vector based sets). Compared to state-of-the-art baselines, the speedup factor in average is 32x for seven bulk bitwise operations while reducing the power consumption by 35x.

==+== D. Comments for author

Ambit is a cutting edge-research paper, written concisely, disclosing ways to improve the current DRAM technology. The challenges are only targeting bulk-bitwise operations.
There is a lack of vectors of improvements in the conclusion at the end. Also, it seems that there is still a huge effort to be made by the industry to push Ambit onto the market, and the simulations of the TRA cells show that there could be yield loss due to the manufacturing process variations, and adding that to the sub-array overhead could push-back the adoption.
Nevertheless it is clear that the energy efficiency and the speedup are non-negligeable for its targeted applications.

# Strength

- Triple row activation with a single address (preselected address)
- Applications can trigger Ambit operations using CPU instructions rather that going through a device API (pluggable on PCIe!)
- Smart Ambit software integration that shadows the B/C rows from the programmer standpoint (easier integration).

# Weaknesses

- Overhead of copying the 2 source rows into the AMBIT capable rows
- Ambit-AND-OR sensible to process variation (affects DRAM yields)

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

no change to the DRAm command and address interfae (no need to go through the GPU and we can make use of the processors intructions)

Reusability across all DRAM vendors due to the same DRAM microarchitectures

Applications mostly for data-centers (we search, genome analysis..)

Baseline of comparision uses SIMD optimizations

TRA -> triple row activations


-- Assume that all the cells have the same capciatance which would not be true in a real design


--- Overhead f copying the 2 source rows into the AMBIT capable rows

introduction of a new primitive operation called AAP
addition of a new row decoder for simulataneous row activations

Row decorder must distinguish between B-group addr adn the remaining ones

B-group, C-group, D-group
C group is controlgroup, with two preinit rows (1111s or 0000s) for controlling the bitwise operation (AND/OR)
D-group rows that store regular data, AMBIT software exposes them only
Ambit controller interleaves the row addresses so all D-group addr are mappped ontiguously to the proc. phys addr space

--- Bulk bitwise operation involves multiple copy operations (can be reduced by compilation techniques)


+++ applications can trigger Ambit operations using CPU instructions rahter that going through a device API (pluggable on PCIe)



Ambit-AND-OR sensible to process variation (affects DRAM yields)

Evaluation with bitweaving (column scan opearations), up to 11.8x speedup
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

13

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

GenASM is the first of its kind Approximate String Matching acceleration framework for genome sequence analysis. It expands the Bitap algorithm to support long reads, unrolls the algorithm for parallelism, and implements traceback for optimal alignment.

There are 3 main use cases for GenASM: read alignment, pre-alignment filtering and edit distance calculation.

GenASM consists of two dependent parts, GenASM-DC (distance calculation) and GenASN-TB (traceback). The former generates bitvectors from reads and accelerates the Bitap algorithm with the mentioned improvements while the latter uses the bitvectors generated by GenASM-DC to find the sequence of deletion, insertion, matches, substitution along with their positions. Both have been co-designed on a hardware accelerator leveraging data-locality, enabling a high degree of parallelism from independent computing units and utilizing HBM for a high-throughput.

The benchmarking shows that the tailored hardware and algorithm in GenASM outperform existing work in terms of throughput and speedup (~x5 compared to hardware baselines and orders of magnitude faster depending on settings for others). The power consumption is also greatly reduced if compared to processors or hardware baselines.

==+== D. Comments for author


# Strength

- Thorough and fair benchmarking on multiple use cases
- Divide and conquer approach and the co-design of the GenASN algo with the HW accelerator which leads to a high degree of parallelism
- Thorough and fair benchmarking on multiple use cases
- Support long reads
- Improves accuracy of pre-alignement filtering

# Weaknesses

- Partial support for more complex scoring schemes

This is a high-quality paper for Approximate String Matching in Genome Sequence Analysis. The Bitap algorithm used as a baseline is well introduced and the vectors of improvements are well described. The figures are helpful for readers understanding. Emphasis has been set on evaluating GenASM with existing work and comparing multiple baselines.

The downside is that GenASM is so versatile with a diversity of use cases that it could prove helpful to explicitely state what future work could be achieved, that which is almost not discussed here.

- (Figure 8. in the GenASM-DC block, at the far right it should be PE64 and not PE65)

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Approximate String  Matching acceleration framewrok for genome sequence analysis
Goal is to design a fast, efficient, flexible framework for both short and long read
Bitap algorithm -> fast & simple bitwise operations to perform approximate tring matching

genasm based on bitap

two modifications 
->(support long reads, // single string matching operation by removing data dependencies)
-> implemented traceback to utilize info. collected ruring ASM for optimal alginemnt

hardware accelerated perfomance modeling

3 use for genASM: read aligneent, pre-alignement fiterring, edit distance calcualation)
100x + performance gain comp. to Minimap2 and BWA-MEM, power reduced by x34 forlong reads, similar for shortreads 

Bitmap limitations 
-> no support for long reads
-> data dependency between iterations
-> no support for traceback
-> limited compute parallelism
-> limited memroy bandwidth

gen asm dc
////
long read support, increase in te algorithm complexeity
loop unrolling
text/level parallelism

genasm TB
intermediate storage with gen asm dc /| divide and conquer approach to reduce memory footprint
partial support for complex scoring schemes

ANALYSIS

+++ main advantage comes from divide and conquer approach and the co-design of the GenASN algo with the hw accelearator
high degree of paralellelism
+++ thorough and fair benchmarking on multiple use cases
+++ Usage of HBM to raise throughput
another error type might lead to a bigger error later on

--- Partial support for more complex scoring schemes

==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

15

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

1

==+== C. Paper summary

Graph-processing workloads are increasing due to big-data. Due to the nature of the algorithms that require neighbor traversal, the access patterns are random and have poor memory locality. Tesseract introduces a Processing-In-Memory (PIM) accelerator to efficiently serve the memory requests while fully utilizing the memory bandwidth to its advantage.

Tesseract accelerates graph-processing through 3 major advancements: specialiazed hardware, a dedicated programming interface, and tailored prefetching. It is architected around vaults that each contain an in-order core, several DRAM banks and a memory controller. A crossbar network interconnects each vault in a 3D-stacked DRAM, commonly called a Hybrid Memory Cube (HMC).

One major bottleneck to achieve higher memory bandwidth is the efficient communication between Tesseract cores. To this end, an API introduces a set of functions primitives to allow for vaults to update/request memory information, carry out core synchronization, and send message-prefetching hints.

The prefetcher mechanism consists of message-triggered prefetching, from the previously introduced API, and of a list prefetcher. The former prevents execution of a non-blocking function call before the requested the memory address is prefetched, which makes exact prefetching without any stalls from the core standpoint. The latter is a stride prefetcher using a reference prediction table (RPT). The prefetching data (start, size, stride) are also passed by the API between vaults and is saved in a multiple-entries list utilized in the for-loops for the RPT (for instance when traversing vertices).

Its evaluation has been carried out with five memory intensive graph algorithms. Performance benchmarking shows that Tesseract implemented on DDR3-OoO, HMC(OoO and in-order) and without prefetching beats other conventional systems, still limited by their off-chip link bandwidth (102GB/s VS 8TB/s for DDR3 and HMC, respectively). Furthermore, the programming model doubles the performance increase and makes Tesseract relevant even when normal architectures hypothetically attain larger bandwidth. Scalability of Tesseract also proves not to be an issue.

==+== D. Comments for author

The in-order core chosen for illustration is a ARM Cortex-A5. Has it been tried with other architectures? Does it affect the overall performance?

The evaluation part wraps up with care all the design variables that could be tweaked and shows that Tesseract still outperforms all other existing configurations. However, there is no mention of the cost of adoption for Tesseract and there is still an overhead due to the new API that needs to be accounted for when designing graph-processing algorithms.

As you mentioned, it would be interesting to dive into how to improve graph distribution across vaults but that is for future work.

# Strength

- Notable improvements under any configuration/workload
- scalability of Tesseract
- close to ideal prefetching (1.8% off!)
- full co-design between HW and API
- below the maximum power density

# Weaknesses

- workload imbalance across vaults depending on graph distribution that could lead to 60% of execution time waiting for sync barriers
- no possibility for address translation inside the memory

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Tesseract (graph processingHW 3d integration to maximize mem BW, efficient communication between mem partitions, 3 a programming interface

baseline improvement of x10 

scalability issue by the memory bandwidth bottleneck (big-data workloads)

access patterns are random

1) development of an efficient mechanism for communication between different Tesseract cores based on message passing.
2) speciliazed HW prefetchers
-> hints given by the programming interface
-> guarantee atomic memroy updates withot requiring software synchronization primitives

GRAPH PROCESING ISSUES

random partenrs due to neighbor traversal, poor memroy locality
increaing the nb of cores is ineffective
HBM helps to some extent, but could be better if doesnt need to use the HBM inter-links

Problematic: how to utilize correctly the large amount of mem bandwidth for efficient graph processing in memroy?

PIm 8TB of aggregate internal BW to the in-memory computation units

TESSERACT ARCHITECTURE

Vault contains 32 ARM Cortex-A5 processors, 16-bank DRAM 
each core can access its local DRAM partition only 
partition a dedicated memory controller
No address translation 

In order cores have o sall on L1 cachemiss which is far from the best way of utilizing th  mem BW

Design of two prefetchers:
- list prefetcher
- message-triggeredprefetcher

Message passig with blocking remote function call
ores swtich states, and returns value queried by the other core

NON BLOCKING MSG
used in conjonction with synchronization barriers

PREFETCHing

List prefetching
- with a constat stride prefetched for frequent sequential accesses

Message-triggered Preetching
for random accesses, a mechanism to use with nb remote function call to indicated prefetching of a certain addr
allows for execution of function ONLY when data is rdy -> no stalls!! and it is EXACT prefetching since we know the ddress needed

TESSERACT API
get, putinterrupt, copy, list begin and end for the list table prefetching, barriers to synchronize Tesseract ores


EVALUATIon
Graph algorithms Page rank, Vertex Cover 

outperforms DDR3 and HMC due to  prefetching mechanisms and the large INTERNAL bw of HMCs as 

LOWER memroy access latency (96%)
one core per vault (32 vaults)

Tesseract + conventional BW with taht of HMC-MC
1.8% off- of their ideal implentation 

scaling of tesseract (512 core systems) is limited bc of off-chip communications overhead due to remote function calls
sub-linear perfomance improvemnt 

employ better data partitioning schemes that minimizcommunicationbetween different vaults

--- workload imbalance across vaults depending on graph distribution   if severe unbalance at the beginning of execution when vertex update happen in a single patition -> 60% of execution time waiting for snyc barriers...
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

2

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Prof. Onor Mutlu gave a broad summary of the data-heavy operations bottleneck in computer architecture. He explained the change of paradigm that is happening from processor-centric to data-centric designs. The end goal is still the same : saving-up on energy, faster computations. He presented a few of the solutions that he has been working on, focusing on data-centric architectures.

He vastly expanded on the memory bottleneck and a few of the introduced solutions have already made their way onto the market or are being worked on and improved at the time being. As the density of DRAM increases, the reliability decreases on the other hand which is why we need to revisit the previous design and processing the data where it makes the most sense, as imagined years ago in A logic in memory IEEE 1970). 

# EXPANDED

The presenter showed  graph-processing examples which are enabled by stacked ICs on top of each other, shortening the paths between the CPU and Data. Other architectures such as GPUs have allowed new-ways of accessing and computing the data, which lead to the push of ML as we know it today.
Examples that were seen: data initialization and bulk copy operations which are usually high latency, high bandwith and cache polluting, can be moved inside DRAMs bypassing the CPU. (details : idea is that we have two consecutive row activations and we make use of the row buffer)
Analog nature of DRAM cells (SIMDRAM, Ambit Architecture) allow any bitwise operations thanks to AND, NOT, OR, thus enabling processing in memory.


==+== D. Comments for author

Challenges presented in this 1-hour overview are already are of importance, but will also continue to be so in the near future as well as in the long-term. DRAMs is the most widespread technology for memories but is still facing issues such as Rowhammer (2014) that drive researchers to find  mechanisms /new ideas to mitigate currents problems and prevent them in the future. The lesson here is that nothing should ever be taken for granted.

I appreciated that the audience was guided and not left behind, thanks to the explanations on DRAM (voltage/rows/columns), however there was no mention of DIMM, Channels, Banks divisions, and it can be tough for a novice to understand the implications of such issues on Rowhammer. Introducing numbers of impacted products, users, and also adding a perspective on how probable it is that the flaw is leveraged by an attack could improve the slightly the overall informative talk.

# STRENGTHS

•	The presenter guided the public throughout the span of the talk and tried not to leave anyone behind
•	There was no focus on a single-aspect, which could make us lose track of the other systems layers. This lead to a better understanding of the improvements that can be performed everywhere.
•	Real examples (UPMEM, Samsung In-Memory) and extra material (with scientific resources) for the curious interested attendees.
•	Several angles of attacks have been presented to reach the ultimate goal : data-driven, data-aware and data-centric
•	Mention of self-optimization of the memory architectures which was not discussed in the presentation

# WEAKNESSES

•	It is hard to define time-scales for changes of paradigms, as a question pointed out.  
•	Lack of precise, detailed examples with specific applications, and more of a whirlwind tour over the solutions due to the time constraints, which doesn’t bring many new inputs for the already aware people
•	Brief overview of DRAM  which to the some people lacking background could be prejudicial
•	No questioning on wether or not the computed data is relevant, which has also been touched in the QA session but the definitive answer if more up to the end user and not if it’s inherently a good thing to discard or scrap out data based on its utility.

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

26

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

3

==+== C. Paper summary

(written in 1968)

The upcoming bottleneck for computer engineering resides in where the data is computed. As the processor's gates scale down and speed will increase, the traditional von Neumann architecture will have a congestion node between the data holding resources (memory) and the computing unit.

The author presents a design in which main memories act as extended cache to which the main processing unit can relay instructions for in-memory computing. This would hide the latency to access slower memories, enabling high speed buffers. He proposes several new instructions that could be issued to remote caches (search on mask equality, masked threshold
copy tag bit, sector ADD/Scale..) to take advantage of the data-locality for certain types of operations (ie. matrix multiplications).

Going forward, we need to improve the programs to instruct them on where to compute the data: distinguishing applications that require high-speed memories and those not affected by conventional slower ones. Lessons need to be learned on how to approach an efficient foreseeing of data movement to not hinder performances.

==+== D. Comments for author



==+== E. Comments for PC

==-== Hidden from authors.

The essay is well structured and shows that computer scientists were aware of this memory computing possibility decades ago.
There is a strong emphasis on the challenges such a system would imply.

It is important that as few as possible control commands are sent ahead to help the cache to organize its data, which would otherwise reduce the benefit of this logic-in-memory.

An understated point is the inefficiency of floating-point computation and how optimizing data-storage in relation to the types could fasten the computations.

I would propose an array of memories where each unit is specialized in a certain type of data (2s complement, floating-point, fixed-point), but with a varying mantissa-exponent / fractional size. Large-scale bulk operations would hence be beneficial for much more applications. This would on the other hand complexify the control logic to decide which memory to use, and also require additional delay/conversion loss when transferring data somewhere else. However the in-memory logic could benefit of streamlined, precise arithmetics even more at the cost of making compiler's and programmer's job much harder. Ultimately this depends on the technology used to store the data, the added overhead and how fast the new system becomes. Which means that there's still a lot of work ahead of us!

The conclusion summarizes very well the tight-coupling between programs and the architecture they run on: keep it as simple as possible. As much as we can improve each block, we as programmers are piloting its actions and those need to be easy to comprehend in order to reach maximum performances of any system.

# Strength

- Idea that "remote" cache can be invisible to program
- Ballpark figures to appreciate the gains
- Visionary essay

# Weaknesses

- Requires an independent mechanism to transfer data in the cache as necessary (today's prefetching)
- On what should we concentrate efforts to achieve logic-in-memory? Vague conclusion

==+== Scratchpad (for unsaved private notes)

The goal is this paper is to demonstrate that the future goal will be to have main memories act as caches.
Logic In Memry arays ould be associative 
could be used for error-code correcting aimplementation and sorting
how a class of logic in memory arrays can be used as high soeed buffer memories 
mempory management tecghniques well proven in practive that hide the latency to access the slower, magnetic drum or disc based memory insyead of the microelectronic technologies

Describes the cache/main memory interfaacer
argues that slwoer memories are still OK because of the cache mechanisms that can be implemented
move instructions issued to the array of caches which are supposed to withhold all the data needed to perform the operations


Proposes new operations with a sector memory address, memory address, operands 

Search on mask equality, masked thresold ( > or >=)
Copy tag bit
Sector ADD/Scale 

Actual utility of aforementioned operations is to be seen, as it is effectively hard for a programmer and a compiler to translate the assembly code into the correct operations to take as much profit as possible of these logic-in-memory.
Shift of thoughts: instructions are sent to control the cache, but rather to manipulaet the data in the memory.

--- mechanism that is indepent is transfering the data uin the cache as necessary ( today's prefetching)


++ cache is invisible to the programs (no control commands sent ahead to help the cache to organize its data)

Mentions the utility for matrix multiplications (ex Gauss-Joradan erduction for matrix inversion)



//// New access mode in the memory
Bit(s) slice of data to be accessed (from multiple words at a time) -? a very large number of words can be accessed simulnateously to peform logical operations, by sector on the data in the cache (mxn opertations SIMUL)0)

Sumarry and conclusion

Diverging from the von Neumann organization, provided that the cost of cache processing remains low
High level languages give a subset of instructions to the programmer and less access to the machine being programmed
parallel development of languages and computers


==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

27

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

MinION, released in 2014, is the first commercially available nanopore-based DNA/RNA sequencing portable device.
The bottleneck for shifting from a cloud computing to an on-board processing has been identified to be the basecalling process which takes up to 96% of the compute time.

This novel alternative to more expensive methods could allow for faster and on-site identifications of future viruses without any requirement of custom primers.

The SquiggleFilter hardware accelerator, based on a Read Until pipeline and Dynamic Time Wrapping (DTW) permits to perform long reads, at a low cost, in real-time using the MinION device.
They implemented several improvements to subsequence DTW (multi-staging, hardware-friendly operations..) which turns out to be suitable for viruses which contain less than 50 000 bases.

The result is a less powering consuming unit (/2), with lower latency (3481x) and greater throughput (x274) relative to existing GPU-solutions.
 
==+== D. Comments for author

# STRENGTHS

- Showed that sDTW shouldn't be eschewed for virus detection
- Huge throughput, latency and power saving improvements
- Power gateable tiles that are independent from one each other
- Accessible and reproducible work

# WEAKNESSES

- There was no comparison with custom hardware accelerated basecalling
- Cost estimation for the custom ASIC needs to be taken into factor when calculating device cost if you include your solution in the comparison

The paper is well written and easy to follow along.
The introduction gave a clear understanding of the challenges and methods currently used, which was required to understand the extent of the work achieved in the paper.

I especially enjoy when more general-devices are reduced to targeted/specific uses cases and it shows that methods that have previously been discarded (sDTW) can prove effective when used appropriately. The bespoke trimmed down algorithm is elegant.

The opening on scalability is appreciated and shows that SF throughput will not be the limiting factor in the future.
However, it would have been appreciated if you would explicitly state what's left to be achieved starting from there because it feels that the paper lacks of an opening.

Some additional comments:
- Figure 16 is great but could be improved because it misleads slightly the reader on what metric should be looked at
- How many tiles could we fit in the design?


==+== E. Comments for PC

This is first-class work that leverages an existing device and accelerates its throughput even more. It deserves recognition and should be accepted.
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

PCR Primers are targeted to a specific virus, and esigning primers is time consuming, error-prone and complex process.
Low cost, portable, and can sequence long reads in real time using Universal PCR that amplifies asll DNA/RNA

Read until, as reads are sequenced, they need to be analyzed in real time

As soon as the computer classifies non viral read,it ejects uit and proceeds to nthe next one

The Deep NeuralN takes 96% of the compute time Large fraction goes to basecalling (96%)

Skip the basecaller by directly comparing each read's squiggles to the precomputed expected signal profuile of the target  entire reference genome

Can sequence in ~2R cycles (R number of bases)

Universal rapid test to determine the whole genome of a target virtus using reference guided assembly

MinION is a portable device able to perform long reads, at a low-cost, in real time 10 samples epr base
The critical computin path for Read Until includes both the basecaller and aligner

Explanation of guppy could have proved useful

SquiggleFilter 
SF diirectly aligns electrical signals read against target viral genome's reference

6-mer / current LUT which provides expected current for every possible combination

--- Not a feasible solution for human genomes (3 billion base pairs)

Multi stage sDTW Filtering -> Non target reqds filtered eand ejected using Read Until would be short
+ absolute difference instead of multiplidation
integer normalizatin ( )

Detect strains 

Measurements -> alignement -> normalization

+++ POwer gating of independent SF tiles
+++ POpening on scalabnility (nanopore chemistr qwith x10-1000 throughput)
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

3

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

3

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

This is a summary writing from Prof. Mutlu about main memory. It gives a wide understanding of the current bottlenecks in terms of DRAM scalability as well as insights into actual research.

The challenges presented orbit around 3 axis:

- new DRAM architectures
- incorporating emerging memory technologies
- predictable performances

Indeed, the growing DRAM density in the sub-30nm technologies brings to the forefront issues in the memory systems such as energy consumption, latency, Quality of Service (effective bandwidth) which are not improving and question the future DRAM usage. Today's trend of ever-increasing the number of processors require the emergence of new technologies to better share memory across cores, and overcome the DRAM limitations.

Efforts have been made to tackle the shortcomings of the DRAM. For instance, Sub-array level parallelism increases bandwidth by allowing to issue two requests to a same bank with less latency. TL-DRAM reduces latency and increases efficiency by dividing into multiple segments the long bitlines. To gain bandwidth and minimize DRAM utilization, Row-Clone exports bulk data operations such as copy or initialization inside the DRAM.

Secondly, the arrival of new technologies questions the two-levels organization in the memory management of persistent and volatile memories. Mainly, Phase-change memory, Resistive-RAM, STT-RAM, each having their specific trade-offs. It is not possible yet to replace all DRAMs with those as they don't accommodate all the needs of DRAMs.

A solution could be hybrid main memories formed by either multiple technologies. The software could take advantage of the different latencies, retention time and power consumptions offered by each technology. Moreover, backward compatibility should be achieved to enhance existing memories.

Finally, the performance challenge is to provide the appropriate bandwidth to each core in heterogeneous systems. The request service rate must be non-interfered to achieve the highest performances possible.

More than ever, the hardware and system co-design is of importance to fully overcome the scaling limits and better coordinate the processors resources.

==+== D. Comments for author

This chapter mentions the challenges in the main memory scaling. It would have been useful to keep track and mention the trade-offs between the solutions presented, ie. which ones are not applicable simultaneously. Metrics and figures were precise and guide well the reader on the points being made.

The DRAM current issues are dissected into several bullet points followed by the introduction of the new technologies. Each section mentions a technological solution to a specific problem, but it would have been interesting to tell more from the application standpoint which for instance has been done for the bulk operations with RowClone.

Lastly, there is a focus on the memory technology but less on the peripheral circuitry changes that need to be achieved as well.


# Strength

- Challenges are clearly exposed, current and future solutions directions as well
- Diversity of exploration vectors
- Aside on flash memory

# Weaknesses

- Underestimation of the efforts required to achieve aforementioned solutions
- Little to no mention of processing in memory
- Which public does it target?

==+== E. Comments for PC
==-== Hidden from authors.



==+== Scratchpad (for unsaved private notes)

DRAM tehcnology scaling issues

shared memory across processing cores
need for an efficient data manipulation
new technologies such as PCM, RRAm, STTMRAM are more scalable
trend of more cores with less memroy capacit, needing for more memory, higher bandiwth

technology scalability (need for finding a technology that is more scalable than DRAM (energy, capacity, cost)

be able to achieve sub 30nm RAMM

need for perfomance predictability and WoS in the shared main memroy sustem

third, need for a much higher energy/power/bandwith


NEW DRAM ARCHITECTURES
1) overcome the problem of refreshment (loss of Qos...),
2) improve reiliability
3) energy efficiency
4) minimize data movement
5) need for a finer garanularity

future DRAM 64gb have 46% refresh rates
approach like RAIDR that puts rows into bins with diff. refresh rates

increase cooperation between DRAM device and DRAM controller to get information about weak cells
easier error management thourgh the DRAM Translation Layer


DRAM PARALLELISM
SALP (sub-array level parallelism to issue two requests to te same bank at the same time) -> introduction of a global decoder


ERNEGY

Solution such as Tl-DRAM with isolation transistors to divide long bitlines into multiple segments to reduce latency and raise efficiency

DVFS can enable dynamic heterogeneity

EXPORTING BULK DATA OPERATIONS TO DRMA
bulk data copy and initialization operations

Row-Clone in-DRAM copy to minimize software impact on DRAM utilization

first class accelerator in a heterogeneous parallel computing system


MINIMIZING CAPACITY AND MEM BandWidth WASTE

low latency data and memory compression (ie. base-delta-immediate compresion) 

better last-level cache writeback (coordinated techniques between the processor ressoures and memory controller)

Challenge 2: EMERGING MEM TECHNOLOGIES

PCM: store multiple bits per cell, non volatile (no refresh!! so low idle power consumption)

cost is much higher latency, energy

reorganizatio of the peripheral circuitry is needed (same for STT-MRAM)

narrow row buffer canr educe main memory dnamic energies


HYBRID MAIN MEMORIES

multiple mem tech merged into 1 (3d-stacked, embedded dram, PCM, STT_MRAM)

software can leverage different rows addr accesses to forward them to either PCM or DRAM part

NVMainMemory
byte-adressable NVM at the downside of security concers: an attacker could leak data after the power is down. (important challenge)


MERGING OF MEM AND STORAGE

reorgnaization of the two levels memroy managemet as seen to merge volatile and persistant memroeis 
todayNVM technology promise persitant data, could make the OS the new bottleneck

ie. Persistent memory mnager (PMM) -> hardware/software cooperation virtual memory system

data mapping

backward compatibility to enhance existing memory

Challenge 3 PREDICTABLE PERFORMANCES
provide appropriate bandwith to each core
able to predict application prefomance in the presence of interference 
(perfomance is a low uninterfered request service rate)

correct rentention errors using Flash Correct and Refresh to increase flash lifitme and diminishus the flash bit error rate

Neighbor-Cell Assisted Correction

==+== End Review

==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

36

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

True random number generation is a necessity in a variety of domains, ranging from security applications, scientific simulation and even entertainment. It is commonly hard to achieve because either it is not fully non deterministic (ie. Pseudo-RNG), have low throughput or depends on a physical process that is not measurable on any device class.

D-RaNGe is a novel class of TRNG which uses DRAM as a medium, widely available on any commodity hardware nowadays (microcontrollers, PC...). It enables a high-throughput (up to 700MB/s), high entropy, energy efficient and stable (non-environmment dependent) source of random number generation at a low-cost.

Certain DRAM cells are vulnerable to activation failures and that is used at DRNG's advantage when those specific cells are being accessed with a lower t_rcd than the specification requires. This prevents the bitlines from being charged back to their VDD/2 voltages, which generates failure and thus randomness.

DRNG work is tiered in two phases. An algorithm finds a subset of cells that are prone to failure, and then a cherry-picks from this set those that fail with high entropy. The second part consist of the serving the requests of random numbers from the host device. DRNG pre-computes random numbers (RN) when the device utilization is low and bandwidth is available, and is able as well to generate RN on-demand while servicing applications workloads with a fast response (max 1us). It requires no hardware redesign as it essentially consists in a firmware routine executed on the memory controller side.

Activation failure characterization showed that from more than 282 devices (either LPDDR3 or LPDDR4) from different manufacturer, under different conditions (temperature, repetitions), the data pattern repeatedly identifies the same failing cells. The entropy is determined (non-voluntarily) at manufacturing time but failing cells are present across any vendors in every DRAM.

The evaluation validates the true randomness with the use of a statistical NIST test suite. Previous work has been using on startup value, data retention time or non deterministic command scheduling but those are respectively unrealistic, too slow and not truly random.

==+== D. Comments for author

A few comments from my reading, for an otherwise clear paper:

- Figure 6 is hard to comprehend, plotting results with T+10, T+15 would allow the reader to easily see the difference
- Paragraph 5.2 could be clarified. lots of algorithms name are thrown in, making it hard to follow
- 5.2 again, does that mean that you need to know in advance which manufacturer it is to select the algorithm? or does it just lead to slightly worse result  

# Strength

- Implementable on any DRAM device
- True randomness and high throughput linearly proportional to nb of banks used
- Works under many conditions (not temperature dependent, t_rcd has a wide working range)

# Weaknesses

- 15 concurrent days of testing only! this might not be enough
- Section 3 and introduction are highly repetitive

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

decrease DRAM row activation latency [t_rcd] to induce read errors (true rng) validated by statistial test NIST

review 284 DDR3 RAM

2order of magnitude higher througput than previous DRAM-basd TRNG (700 MB/s)
Pseud-random number generator (from a seed)

1. implementable on commoditiy dRAM dvices today
2. fully non deterministic
3. provides continuous high thoruphut
4. doesnt affect running applications

OBSERVATIONS
certain cells are vunerable to activaio failures
-> identiy them using a low latency profiling step

15 day of testin, w/ != range of temp 

TRNG
1) entopy source
2) randomness extraction technique
3) post-processor to improve randomness of extracted data at the expense of throughput (REMOVES CORRELATION)

Section 3 is highly repetitive

5. Acivation Failure Characterization
spatial distribuion of activation fialures
data pattern dependence on DRAM cells
temperature variation

SPATIAL
failure prob. of a cell attached to a btline correlates with the distance between the row and the local sense amplifier
1) regon AND bitline of DRAM being accessaffect the number of observable action failures

DATA PATTERN TO IDENTIFY CELLS PRONE TO FAILURE
different data patterns result in diffeent failureproabilities
temperature affects F_prob to different degrees, but generally incraeasing T incresae the F_prob

entropy is deterinisic at manufactuing time long term aging effect are not studie

DRNG
1) finding a subet of cells that fail with 50% prob and then the subset that fail with high entroy

1000 reading with reduced t_rcd
approximate each cell's Shannon entropy by countin the occurence of 3-bit symbols across its 1000 bit strea. RNG cells are the ones that have an equal number of 3-bit symbols

--- only 15 days of aging tested....

DRAM access can induce activation failures only in the acceessed DRAM word -> the denstiy of RNG cells per DRAM word determines the number of random bits D-RaNGE can generate per access

READ requests NEED to follow an ACTIVATION (need row conflicts
)

queue of already harvested random data may be maintened in the memroy contoller for use, and harvest data only when DRAM is not harvesting other requests

EVALUATION
passess all NIST tests -> fully nondeterministic

RNG cells are widely avaialable across all manufactured DRAMS across ALL manufactures in all banks
wide range of t_rcd possible (6-13ns compared to 18 default)

++++ throughput is linearly proportional to the number of banks used
latency is DRAM access latency 

low storage overhead (0.18%)

PREVIOUS WORK 
non deterministic command scheldling but NOT fully non determinististic entropy source)

DRAM data retention -> too slow! 0.05 MB/s
DRM startup values
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

37

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

3

==+== C. Paper summary

This paper presents a self-optimizing memory controller that takes effect on the scheduling policy. Static policies such as FR-FCFS do not adapt to switching workloads, which is where reinforcement learning (RL) methods come in to perform on-the-fly policy changes.

An RL-based memory controller monitors its environment and performs actions (sends commands) relative to the current states (open rows, queue, time of arrival...). The RL controller should not violate the specification timings. Its goal is to prioritize the long term cumulative rewards by learning an optimal scheduling policy. The RL agent is also be able to allow for a certain degree of freedom by scheduling random non-ideal immediate commands but potentially better rewarding in the future.  

The optimal policy algorithm uses the concept of Q-values that represent state->actions pairs, constituting the scheduling policy. After each command issued, the Q-value is updated (rewarded) in function of the new state, the previous action executed, and the previous Q-value. To summarize, Q-value is the expected outcome of the cumulative discounted reward that is obtained after a specific action is executed in a given state. Discounted means that infinite rewards are not possible and each Q-value ends up converging. It is a guarantee that in the long-term, the controller will end up with the optimal policy.

Techniques such as CMAC save SRAM space to store the controller's Q-values while giving a trade-off between coarse and fine granularity. This is necessary due to the exponential number of required Q-values, growing in function of all possible states and actions.

This is also why a preselected optimal set of  states is used,  with the benefit of not impacting the results when evaluated against more states. Baseline FR-FCFS policy is topped by RL-agent (min. +5% bandwidth) across all workloads, with an almost ideal data-bus usage (80%) which is a reliable indicator for performance.

==+== D. Comments for author

The idea of CMAC is very interesting and brings a lot to the implementation of the RL-agent in the hardware. The paper is rather concise and well-written but I feel that the evaluation has focused too much on a specific workload, which the opposite of the versatility RL is intended for. Figure 12 could help showing that.

A few comments:
- No evaluation on reactivity for workloads change has been performed
- If you mention multiple controller, a conclusion opening would have been appreciated on ideas to coordinate them rather than concluding on their autonomy 
- why does offline RL perform better than FR-FCFS? it seems biased because you supposedly trained it before. 

# Strength

- CMAC Q-values subarray division
- improvements compared to FR-FCFS
- number of selectable Q-value per DRAM cycle does not affect too much the outcome

# Weaknesses

- No evaluation on reactivity for workloads changes (how long does it take to switch to a policy better performing than FRFCFS)
- Fairness has not been evaluated
- e, alpha, gamma parameters were not enough evaluated


==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Self optimizing memory controller (scheluding policy)

reinforcement leearning to overcome dynamic workloads imitations
on-the-flyoptimizations
4-core CMP improvement by 19% in aveage

chip multiprocessors

off-chip bandiwth might soon become a limitation as number of pin is reaching a threshold

ad-hoc memroy controller designs

CONTroLLER
RL-based memory controller considers the long-term perfoamcne of impact each action it can take


2) take actions that provides the highest long-term reward
3)update long term reward values associated with state action pairs based on feddback from teh system

DDR2 dual channel dram

DRAM chips needs to obey DRAM timing to provide correct functionality

controller must prioritize DRAM commands from diferent memory requests to optimize erformance

FR-FCFS does not consider the lon-tern perfomance impat of priritizzing a column command ovre a row one


REINFORCEMENT LEARNIGN

agent sense the current state and executes an action
goal: maximize long term cumulative reward by learnin an optimal policy that maps states to actions

rewards can be deign i several ways depending on optimization goals (maximize data bus utilization)

3 challenges
1)temporal credit assigment (for bad past decisions, and predict future decisions, and anticipation for long-term cumulative payoffs
2) exploration VS exploitation: agent needs time to learn about its environment but also should give the best availalble policy at any time

Markov decision processes

next sate in DRAM scheduling may depend on the command scheduled by the DRAM scheduler and also y the system behavior that one can learn its function

CUMULATIVE REWARDS
convergence knob to prevent infinite rewards

Q-VALUES
q value of a state-action pair under policy \pi represents the expected value of the cumulative discounted future reward that is btained when action a is executed in state s

it descrivbes te long term value of scheluing a command in a gven syste, state

STATES
6 attributes considered 

-> optimize the read/write balance
-> detect low levels of request concurency n the transaction queue
-> facilitate learning
-> amortize write to read delays by satisfying writes in bursts
-> approximate nb of critical requeusts that might block the queue

assume an integrated on-chip memroy controller

ALGORITHM
the goal of the algotirhm is to pick the command wwith the hgjest q value for schedling

Q-value update based on the update rule known as the SARSA update
empirical methods to find alpha, gamme and Q

guaranteed to find the optimal scheluding policy wih probability 1

--- not aggressive enough maybe
e greedy action selection (random command with a small probability

GOAL: reduce number of Q values

quantiye the state space into a small nb of cells with a single Q avlue to reduce storage requirements

CMAC balancing generatlization and resolution
multiple coarse grain Q value tables shifted by a random amount, used to represent a higher number of Q-values with a smaller number of cells

hashing can be used (inputs are states) to reduce storage

ENSURE CONTROLLER PROGRESS
no nops
not allowed to activate unsolicitted rows
able to escape starvation due to lock mechnamisms issuesing multiple time the same mem req.
timeout policy
Rl cnnot dictate refresh interval

HADWARE

each CMAC array is an SRAM array f 256 Q values, 32 CAMC arrays in each..


can compute two Q values per cycle, 10 cycles between eah DRAm cycle and 4 cycles necessary to ill up the pipe, so 12 Q-values can be considered each time

floating point arithmetic to compute Q values

32kb on chi storage for 8192 Q values

EVALUATION
evaluation of the hundreds of attributes to find the 6 best perfoming ones

perfomance improvement of 20% (5% min. for all applications) with baseline Fr-FCFS

%0% improvement of the data bus!! 

dual-channel compatibility


--- perform multi-controller coordination in future work
---why offline RL performs better than FCFS? that doesnt seem normal
--- how to find alpha?

---sensitivity (reactivity) to workload change
--- fairness problems
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

45

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

The main memory is nowadays shared by multiple cores and the physical memory is split across multiple memory controllers (MC) that all should service the applications loads and stores. The three main goals in designing memory controller's algorithms to service requests are (1) provide consistent performances regardless of workload (2) maximize instruction throughput and (3) minimize synchronization overhead across MCs.

ATLAS can be summarized in the following way. It divides the time into a quantum that is itself split into long quanta.  It introduces the concept of least-attained services (LAS). Every MC is responsible to compute its local LAS for each thread, which is how many times it served a memory request for a thread (higher ranked means less memory requests serviced for this thread). At the end of each quanta, every MC reports to a meta-controller the LAS for each thread. The meta-controller weights sums them and merges the previous ranking computed by the last quanta during quantum. The final ranking for threads that it sends back to the MCs for the next quantum. When choosing which request to handle, ATLAS follows a policy of least-attained thread first, and then uses regular FR-FCFS. This allow for coordination across MCs that take into account the long-term memory intensity of each thread rather than a finer granularity. Additionally it services first the requests that have been outstanding for too long to prevent starvation.

Over a long period, ATLAS increases the computing units throughput by minimizing the amount of time spent stalling for memory requests. Compared to state of the art PAR-BS, FR-FCFS, FCFS (in decreasing performance order), ATLAS instruction throughput is always higher for any workload and the improvement should be even more noticeable as the number of MCs increase.

==+== D. Comments for author

Long batch durations are a bit counterintuitive as finer-grain approaches could seem more versatile to reduce memory episodes. ATLAS chose to have a different perspective, and this in fact is maximizing the long-term as it has been demonstrated on the benchmarks. While I was reading, I came across several points: how to determine best-performing values for T, alpha, and the number of cycles for quantum and quanta, which have all been answered later on.

Overall the paper goes straight to the point and does not loose the reader or overflows him with insignificant detail. 

On the minus side, Figure 7. could plot the increase in atlas speedup for 1-MC, 2-MC 4-MC 8-MC and 16-MC (compared to ATLAS itself for less MCs)

Additional comment:
- Figure 10)b) color ordering is hard to read

# Strength

- Simplicity of the ATLAS in general
- Performance gain compared to PAR-BS (best in class)
- Scalability
- T, alpha, and quantum periods have been tested for a vast range of values
- evaluation of uncoordinated atlas for thread ranking

# Weaknesses

- Empirical determination of thread weight by the OS? (even though mentioned in 7.6)
- Alpha close to 1 could lead to attacks by certain threads (slowing the instruction throughput) as it is unfair to memory demanding threads

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

multiple memorycontrollers to control access to main memory
with coordination accross controllers

improves system thoruhput

least attained service 

multiple memory controllers are used to access a larer physical memory

thread ranking is computed at the beginning of everyy bach of requests (apporx. every 2000 cycles

per thread information within each controller need to be broadcasted to al controllers OR  global  meta controller needs to gather info, compute ranking and broadcast it to all controllers


ATLAS
Lest attained service base thread ranking o maximize system throughput
long time quantum to provide scalaility

execution time is divided into qunta

controllers coordinate to determinea consisten ranking of threads

threads that have attained the least service from memory are ranked highest

every controller uses this ranking to prioritize higher ranked threeads' requests

->scalabilitybc of long quanta ->ensure that information exhcnage is scarse
->starvation freedom by using thresholding (forrcesthe servicing of a request that has been outstanding for too long)

when controllers are aware of each others' state, they can take coordinated actions that can improve system performance

pareto distribution: P(Job > x) = kx^_-\alpha 

MECHANISMS
a thread alternatates betwen
1)memroy episode where the thread is wating for at least one mem. req
2) compute (o mem req)

prioritize thread whose mem episode will end soonest

attained service -> total amount of mem service that a mem episode has received since it started

quantum is a longer period divided into quanta. this is to ensure equity between threads as one could have lots of mem req but then nothing for a long period, whereas thread A could be lots of short mem req pulses.. 

coordination ath the beginning of a quantum for coordination across threads

two majros benefits:
maximizes system thoughput within a quantum by minimizing the time spent in memory episodes

ATLAS has thresholding for non starvation guarantee
addition of thread weights as well

no previous memroy scheduling algortihm tries to prioritize threads by taking into account their long-term memory intensity

+ long batch duration

---- empriical determintion of T, alpha, thread weight

each memroy controller as a local AS value for each thread

each thread's local AS value is sent to the meta controller and then reset to zero

meta controller keeps he totalAS value for each thread and updates it

EVALUATION
memroy intensive and memorynon intensive

PAR-BS assumes to have constant global knowledge which is highly unrealistic BUT ... provides an upper bound on whats achivable 

higher instruction throughput 10.8% comapred to PAR-BS and 7.5% to the idealized PAR-BS. perfomance increase constant accros all workloads

STFM poor results because MC are not coordinated, so the threa slowdown value is innacurate

Efect of memory intensity n thw rokload
-> atlas performs well when the workload is heteregonous

if workload consists of all memory intensve or all memoy non intensive threads then ATLAS performance s less pronounces bc 


+++ uncordinated atlas evaluation for thread rankng

Figure 10)b) color ordering is hard to read

value of a can lead to attacks denying access to other theads

atlas is ufair to memory intensive threads that are likely to be less affected by additional delay than non intensive ones
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

62

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

3

==+== C. Paper summary

Although the cost per bit in the DRAM technology has decreased by 16x, the access latency has remained relatively constant throughout the years (30% reduction). This bottleneck is caused by long bitlines in the subarrays of DRAMS to which cells are attached. Their long length increase the line charge time to reach VDD/2 again for the sense-amplifier after a PRECHARGE command (which isolates the bitlines from the cells after a reading). The combined capacitance of both the cell and bitline parasitic one impact the timing constraints.

The key idea in Tiered-Latency DRAM (TL-DRAM) is to divide the bitline into two sides by adding an isolation transistor which adds a high impedance from the sense-amplifier standpoint and keep the cost-per-bit stable. This reduces the seen capacitance for cells closer to the sense-amplifiers and thus the access latency. The two sides are denoted as the near and far segment. The notable downside is an increased power consumption and access latency for the far-segment.

To circumvent this, the goal is to access more rows in the near segment than in the far one. Efficient cache management could take place by doing an OS-transparent hardware managed cache, or letting the OS access the near-segments. Three cache management algorithms (LRU-cache, Wait-Minimzed Caching and Benefit Based Caching) have been evaluated for the OS-transparent one. The OS-managed method was tested with an exclusive cache and a profile-based base mapping.  An intelligent inter-segment data transfer without additional overhead on the die, reusing the capability of the sense amplifier was used to not go through the DRAM controller to move data between near and far segments, which would drastically increase latency and cut off the segmentation benefits.

The evaluation uses multiple DRAM-benchmarks to find the best-fitting ratio of near-to-far segments for a fixed number of cells per bitline. As an example, it is showed that for a fixed sized of 512 cells, an ideal number of 32 near-segments improves the performances by ~10% compared to the baseline. The OS-managed near-segment thorough testing has been left for future work. The main conclusion is that there's a trade-off between the number of near-segments, the cache algorithm used and ideal latency. However, the overall power is reduced because of the higher number requests serviced by the near-segment.

==+== D. Comments for author

Partitioning the segments into more than two could further improve the performances, at the cost of ever-increasing latency for further segments and algorithm complexity for cache management. It would be interesting to try out a 3-segments DRAM for instance.

Enforcing a near-segment cache policy might not be the best way to deal with fast-switching workloads (ie stream then random).s

# Strength

- Efficient strategy with lots of areas for improvement (cache policy)
- Low area overhead for the isolation transistor
- Inter-segment data transfer in DRAM
- Concise paper, reader is not lost in the explanations

# Weaknesses

- Weak evaluation of Profile-based page mapping
- No appendix on equivalent bitline capacitance computation (w/ or w/o isolation transistor)

Additional comment:

-Figure 14. summarizes strongly performance improvement of TL-DRAM!

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Tiered latency DRAM

memroz latency of DRAM has remained constant, beocming the bottlneck
key metric is the DRAM latency decreased by 30% while the cost per bit has decreased by x16!

long bitlines are the dominant source of DRAM latency

each bitline is split in two with the use of an isolation transistor

near segment VS far segment

isolation transistor is turned of for the near segment, sense amplifier only sees this side of the load (at the cost of inreased latency in the far segment due to the extra load of the transistor)

near segment is used as a hardware managed cache in the DRAM
MC maps pages into the near segment, and one where OS does profiling to map frenquently accessed pages to the near segment

bitline at 0.5 VDD. when access transistor turned on, either goes to 0.25 or 0.75VDD. then the sense-amplifier amplifies tue perturbation and injects charge into the cell capacitor and the bitline parasitic capacitor. The cell charge is then restored to its initial value

PRECHARGE turn off the access transistor so the cell is decoupled from the bitline and is not affected by future changes in the bitline voltage

sense amplifier injects charge from the bitline parasitic capacitor to reach 0.5VDD again.

BITLINE LENGTHS

aggregate capacitance of bitline and cell determine how fast the sense amplifer charges the biltline to VDD/2

DRAM area size is inversely prop. to numb of cell per bitline

PLOT of segment length for a fixed max nb of cells per bitline

1.83% overhead for a single isolation transistor

INTER SEGMENT DATA TRANSFER 

data must be read out to DRAM controller and written back
TL-DRAM connects the cells in both near and far semgnet before another activate

LEVERAGING TL_DRAN

1.OS-transparent cache

near segment as an MRU cache

WaitMinimizedCaching (two consecutive accesses)
cache the first access in the near-segment to minimize the seond access latency, and then serve the first

benefit based caching
keep track of cycles benefits (in terms of DRAM cycles saved for subsequent accesses and latency reduction)

2. OS-Managed segments 
exclusive cache
-> managed with a simple policy at the cost of overhead rows (dummy, to-be-cached rows), 0.2% of a subarray

profile-based page mapping
-> bits reserved in the physical address for the segment magement
introduction of an additional near segment row decoder to activate two rows at the same time

--- additionnal power due to isolation transistors
--- Underevaluation of Profile-based page mapping
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

63

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

2

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

(Written in 1979)

This brief note from Prof. Amdahl illustrates the necessity to give more thought on whether or not multi-core processing has benefits compared to the traditional single processor approach.
He states that not every program can benefit of the multi-processors, one memory, as the instruction stream will stall due to memory congestion.
He shows that although there's use for this new method, due to overheads in sharing, wait time for serial instruction cannot be ignored, and there is an inevitable slow down.

The conclusion is that the gain is not only dependent on the number of processors, but rather to the percentage of the program that can be parallelized.
It can be seen that adding N processors does not scale the throughput by a factor N, as opposed to having N processors executing the same program on different machines. 

==+== D. Comments for author

It's a fair point that tradeoffs are to be expected when talking about multicore processing and the workload is hard to balance equitably across the computing units.

What to consider when developing program for multicore processors? Where should be the focus: in the hardware to handle multiple memory requests to keep a certain level of fairness, or to have instructions that better structure the programs to make use of that new efficiency.

In conclusion, it lacks of inputs for vectors of improvements to the new approach and there is a feeling that we are only itching the surface.

# Strength

- Examples are precise and illustrate correctly the bottleneck

# Weaknesses

- (graph hardly readable)
- "Blanket statement" in the conclusion without proposals for future work

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

written sept 1979

Validity of single-core processors VS multi-core processors

Argues about the need of achievements in quential processing raets 

"If it were easy they wouldn't have been left as bottlenecks"

==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

64

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Programs are written and run sequentially on so-called sequential computers. However, the gain in performance is decreasing as the programs get longer. The multiprocessors era's goal is to execute sequential programs on several processors at a time, splitting the workload and the memory banks at the same time.

The challenge is to guarantee identical executions and end results each time the program is run. This is increasingly difficult as the ordering between operation (memory fetches and stores to any cell) matters to computing operations, and number of processors in a system increase.

The term sequentially consistent, introduced in this essay, means that a sequential execution on a single processor should yield the same output as a multiple cores execution.

With a set of two rules, (R1) each processor issues memroy requests in the order specified by its program and (R2) memory requests to a module are serviced by a FIFO buffer, it is shown that this sequential consistency can be achieved.

Conclusion is twofold: verifying the correctness of execution is a burden and multiprocessors programming should be done at the lowest level to achieve best performance.

==+== D. Comments for author

This is an informative note about sequential consistency, and illustrates well the problem with critical section that it is trying to solve in order to achieve true "parallel sequential" execution.

As it is a very brief explanation, there's no order of magnitude computations involved (ie. slowdowns due to R1 and R2, or speedup by servicing store/load not using FIFO order)

We could also mention memory barriers, but the added-value is excluded as in we only consider inter-processor communication done through memories.

# Strength

- Sequential consistency for critical sections
- Mention of other possible improvements to presented protocol
- Brief but concise

# Weaknesses

- Lacks a proper conclusion

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

large sequential computers exeecute operations in a different order than the one specifiedby the program

multiprocessor computer a correct execution by each processor does not guarantee the correct execution of the entire program

squentially consisten 
-> the result of any execution is the same as it it were executed sequentially

interconnecting sequential processors wth memroy modules that insures the sequential consistency of the reulting multiproessor.


computer consists of a collectio of processors and memroy modules

operations of cencoern are the fetch store req to mem

critical section -> only one process is executing it aat any time

to minimize waiting, a processor can issue a store request without specifying the value to be stored

R2: memroy requests from all processors issued to an individual memory module are serviced from asingle FIFO queue
R1:Each processor issues memroy requests in the order specified by its program

if FIFO contains a store with non received data, the memroy is idle. R2 can be weakened to allow the memory module to service other requests (not in the same memroy cell)
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

65

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Performance bottlenecks of critical sections in multi-threaded application cause a serious issue in CMP architectures. Accelerated Critical Sections (ACS) is a novel method that aims at shifting the execution of the serial critical sections onto a larger core, improving scalability and overall speed of the program execution.

Over any workload (coarse or fine grain locking), the methods has proved being efficient with an average of 34% faster execution time on the different programs used to benchmark ACS.
Simultaneous multi-threading and Selective Acceleration of Critical Sections (SEL) allow the large core to prevent creating more bottlenecks in the critical sections execution requests issued by smaller cores. SEL detects false serialization and decides whether or not to execute a critical section on a large core.

The authors compare their work with the most resembling methods (improving locality of shared data and locks, RPC), but shows that although they are analogous, ACS comes out as the best method to accelerate shared-memory parallel programs.

==+== D. Comments for author

# Strength

- No specific overhead for the programmer -> the compiler does all the job for you (ISA extension)
- ACS becomes more attractive as the area budget in terms of cores increases
- No cache transfer overhead as locks are kept to the large core (CSCALL/CSDONE advantage) (no thread context migration)

# Weaknesses

- Delaying critical interrupts to prevent deadlocks when waiting for CSRET is a major drawback
- Lack of opening on scaling the method to a higher number of large cores

- No availability of the code to reproduce the results?

The paper includes lots of figures to backup their claims with numbers, and it shows that extensive benchmarking has been achieved in order to prove the method. ACS is well described and this in an interesting mechanism with which also has positive repercussions such as eliminating transfer of data across caches. This ultimately lowers the number of cache misses.

The only big concern that is left is: is delaying interrupts the best way to prevent deadlock mechanisms? As this potentially could delay critical inputs and there doesn't seem to be workarounds/ways to ensure that this is not happening with ACS.

A few additional remarks.

- Section 3.9 is short / wouldn't the presence of more large cores be equivalent to the initial problem set? 
- 8.4 even if RPC is intended for network programming, it would have still been interesting to compare it to ACS
- what is the area of a large core compared to small cores?

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Chip-Multiprocessors that provide multiple procesisng cores on a single chip. 
Applications create threads that operate on the same problem and communicate with different portions of a shared memory
Critical section -> only one thread can execute it a time
accelerating executions of critical sections can improve performance and scalability
accelerated critical sections are executed by a large core and notifies the core that requested execution of the instruction
private data is transfered via the regular cache coherence mechanism
ACS reduces the number of L2 cache misses inside the critical sections by 20%

--- false serialization
-> dynamic mechanism that decides whether or not a critical section should be executed on a small core or a large core

+++ new instructions CSCALL [LOCK_ADDR, TARGET_PC] 
                     CSRET  []

Compiler removes register dependencies and inserts those instructions around the critical section

CSDONE response when large core responsd to small core

Critical section request Buffer pensd CSCALL requests sent by small cores, size is * to # cores ( storage overhead of 300 bytes)

Chip-interconnect modifications to support extensions

Simultameous Multi Threading and Selective Acceleration of Critical Sections (SEL)

Selestimates the occurence of false serialization and decides whether or not to execute a critical section on a large core
if the occurence is high, the serialization is executed on the smaller core
reset the ACS_DISABLE bits every 10 million cycles to adapt to phase changes

--- delaying critical interrupts to prevent deadlocks is a major drawback

Transfer of cache data

+++ no cache transfer overhead as locks are kept to the large core (CSCALL/CSDONE advantage)

+++ ACS becomes more attractive as the area budget in terms of # of cores increases

Coarse grained locking improvements (qsort and tsp havs smaller perfomance boosts)
Fine grained locking -> ACS wastes most of the area budget by dedicating it to a large core because it is unable to use the large core efficeiently

ACS Perfomance increases as the area budget increases
ACS with SEL outperfoms w/ SEL by 15%, reduction in average of 34% over the programs benchmarked

+++ No migration of thread contexts aith ACS


==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

66

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Published in 2014, Rowhammer is a widespread disturbance in all DRAM that breaks memory isolation and allows an attacker to induce bit-flips in victim rows by accessing adjacent rows frequently in a limited time period (known as hammering).

As the DRAM cells continue to scale down, Rowhammer worsens and the vulnerability increases as the cells get closer. Several level of mitigation have been planned out, (1) increase the refresh rate, (2) isolate the rows with physical addressing, (3) refresh rows and lastly (4) a proactive throttling of the memory requests.

Ideally they require no modification the the DRAM chip design, no impact on performances or energy consumption, a reliable security by fully mitigating the attacks, as well as not throttling benign applications. Preventing Rowhammer is difficult as existing solutions all show that trade-offs need to be made in the previously mentioned metrics.

Blockhammer is a defense mechanism implemented on the memory controller that uses low area (<1%), saves energy (34%) and is better performing than state-of-the-art mitigation. It relies on two mechanisms:
- A rowblocker that prevents accessing row after a certain activation thresold in a time window
- AttackThrottler, which tracks <thread, DRAM bank> pairs to detect threads that are rowhammering to slow them down  

It is a promising defense mechanism that was proof-tested on many sided activations, scalability and benchmarked against all state-of-the-art solutions.

==+== D. Comments for author

The paper is rather dense but of impeccable quality. Blockerhammer seems to be an effective prevention of Rowhammer. The paper presents two main tools to achieve at its results, but the focus is really Rowblocker. Attackthrottler (AT) is an additionnal defense mechanism, that helps out the former. AT could be highlighted in the conclusion for future-work direction.

AT also doesn't find patterns where different threads interlap their rows accesses. So in this case AT would have limited to no impact.

Blockhammer is elegant as is doesnt not induce row refreshes, saves energy and doesn't require to modify the digital design nor entails a large area.

The latency of Rowblocker was also computed and it shows that is two order of magnitude smaller than the row access latency, which further validates usability of Blockhammer

For the many sided pattern, it is not clear from a first reading that Nrh* becomes the new Nrh for every pattern.

As for the scalability, I was trying to find the reason why the area increased when Nrh decreased. This because the CBF storage must increase to prevent faults and rows bits overlapping. This makes the evaluation results a bit harder to understand for a first read, perhaps this could be mentioned again in the paragraph below Table 4.

# Strength

- better results than state-of-the-art-defenses and scalable
- area efficient, no dram redesign, no performance degradation
- effective against many side rowhammer attacks
- latency analysis
- (figure 2 and 3 summarize very well Blockhammer)

# Weaknesses

- AT could be bypassed by multi-threads attacks
- (Section 5 is confusing; needs rephrasing or illustration)

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

BLockHammer

Rowhammer, bit flipping to escalate privilege nd leak private data
Rowhammer mitigations require CRAM chip phyical circuit layout OR modification to the DRAM chip design

blockhammer low cost mitiation mechanism to prevent all rowhammer bitflips

1) track row activation rates using are efficient bloom filters 
2) use tracking data to ensure no row is ever activated rapidly enough toinduce rowhammer

four level approach
1)inreased refresh rate
2) physicial isolation
3) reactive refresh
4) proactive throttling

challenge 1: efficient scaling as rowhammer worsens
challenge 2) compatibility with commodity DRAM chips

BH provides better performace and energy (avg max of 45% and 34%)

1)false-negative-free variant of counting bloom filters that eliminates the need for per-row couners
rowblocker blacklists the row until the end of the time interval

attackthrottler  reduces the memory bandwith consumed by an atacked by reducing the mem bandwith consumed by an attacker, therebey allowing concurrently 

---benign VS attacker, distinction?

attackthrotller expose the rate at which trhead activates a blacklisted row to the OS for better scheduling

ROwhammer likelihood inde

blockhammer is implemented in the memroy controller

--acctivation rate
--rowblocker delay??

Unified bloom filter -> two bloom filter with one reseted every epoch
Counting bloom filter -> returns the smallest numbe in a BF elements

combines both unified bloom filte r and counting bloom filter for blacklisting

-min of 2 epochs

Rowblocker HB is a circular queue that store row ID, timestampand  valid bit.

Tnuning for different DRAM standards


ATTACKTHROTTLER
-> identify and throttle threads that potentially induce a rowhammer attack

a thread that attemtps to issue more activations to a blacklisted row is flagged as an intrusive thread

applies  quota to the total nuber of in flight emroy requests allowed for an thread identifeid to be apotential attacker


rowhammer likelihood idex (RHLI)
<thread, DRAM bank pair>
trackers the number of blacklisted row activations the thread performs to the DRAM bank

---muli thread mitigations for attackthrottler???


+++ many-sided rowhammer attacks
---to take into account Nrh you need to increase the counter granularity (to count for sub 1 activations), this was not mentioned?

when RhI exceeds 1, attack throttler blocks  athreads memroy accesses to a bank

observe only and full functinal
observe nly show close to 0 RHLI for benign and 10 for Rowhammer inducing ones

OS-level mechanisms using RHLI for future work

SECURITY ANALYSIS


HARDWARE COMPEXITY ANALYSIS
performed with two rowhammer threshold, 32k and 1k

latency analysis -> 0.97 ns, two order of magnitude smaller than the row access latency (50ns)

scalability
blockhammer is highly scalable as Nrh decreases

worst case latency observed is at least two orders of magnitude smaller thn typical QoS
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

67

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

3

==+== C. Paper summary

Conventional prefetchers suffer from a few issues: (1) lack of adaptability, (2) no system awareness and (3) only 1 pre-defined parameter is chosen for the prediction. They hold a core role in microarchitectures and are essential in order to have energy-efficient, low-latency and high throughput cores. Those prefetchers are designed to perform the same under any workload and number of cores.

Pythia implements a configurable reinforcement learning agent on hardware, and although not as general-purpose as ML to explore diversity of configurations, it provides an area-effective prefetcher that improves perfomances, accuracy and latency.

It outperforms other state-of-the-art prefetchers (MLOP, BINGO, SPP..) and its gain is linear to number of cores.

==+== D. Comments for author

The Q-value division in vaults is a great way of achieving lower storage space, and reminds the CMAC technique in review [37][Self-Optimizing Memory Controllers: A Reinforcement Learning]. Action pruning is a clever way to prevent exponential explosion of the array size. The pipeline for Q-value updates is a welcomed addition as well.

The main downside of automated design space exporation is that it has been done before configuring Pythia for online use, so it seems to be offline DS exploration for an online use. As you have written the features selected are the best-performing ones but also later it is stated that for Ligra worload, the feature selection and reward should be adapted. As far as I understand Pythia is not capable of doing that online.

An explanation of the XOR's in the program features (3 and 7 table 3) could enlighten the readers.

In the algorithm, the Evaluation Queue is an ingenious implementation of the reward system and the 5 level of rewards (especially the no-prefetch) demonstrate their use later in the paper. Would tuning the reward values together rather than individually lead to different results?

The use of unseen traces is a reliable method of showing Pythia's perfomances.

In the evaluation, the power-overhead is not compared to the power-savings of the Pythia solution compared to others prefetchers.

In the multi-level caches, only Pythia+stride have been tested, but could Pythia+Pythia lead to even better results?

# Strength

- Action pruning to save space
- Pythia evaluation using champsim, and perfomance increase
- ++ Tweakable through registers for feature selection and rewards
- Small area and power overhead
- Clever evaluation queue reward system and pipeline

# Weaknesses

- Multi-level prefetching schemes were not evaluated thoroughly
- Pre-training of Pythia for feature selection sorts of defeats the purpose

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

harwdare pretching techniques
PC, cacheline address, or delta between addresses
neglect mem BW or system unaware prefetch algorithm

reinforcement learning agent pythia

program context is a feature

PC, Address, Page offset of a cacheline

prefetcher accuracy reduces the long memroy access latency of the processor

CURRENT PREFETCHER LIMITATIONS
1)use of 1 program feature for prefetch prediction
2)no ystem awareness
3)lack of adaptabilitiy

PYTHIA
silicon customized vi configuration registers (incr/decr. coverage accuracy, timeliness)
state/agent systm with a reward system for prefetch and non-prefetch

learning rate parameter

RL better than machine learning as model size exceed largest caches in traditional processors
quick predictions

PYTHIA
find the maximal prefetching policy that would maximiye the number of accurante and timely prefetch requests

states are a k-dimensional vector of program feautre.
a progrma feature is at most 1(porgram control flow component AND/OR rogram data flow component)

PCF uses PC of a load instruction, branch PC, and history to remember if info is extracted only from the current demand request or a serie of past req

PDF is cacheline address, page offeset, cahce delta, and history..

pythia has a fixed k dimension (limited HW size budget)
5 level of reward 
accurate and timerly/late, loss of coverage, inaccurate
no-prefetch

Q-Value
Evaluation queue has entries
(1) take action, (2)prefetch address gennerated  3) a filled bit (pref req has been filled into cache)

for ever y new demand pythia check the EQ and attributes rewards

EQ evictions are used to updae Q values

QVStore search
table based hierarchical QVS store
k partitions (vault)
each vault is a constituent feature of the state-vector and records te Q values for the feature action pair Q(\phi_s^i)

a vault is a two dimensionnal table indexed by feature and action values

problem is size of the table is exponential
-> tile coding (CMAC)

multi stage pipeline to retrieve maximum Q value
+++ area andpower overhead of the pipeline

reward assignement and Q valu updates
1) immediate reward assignement during EQ inserstion
2) during EQ residency
3) during EQ eviction

pythia outperforms bingo and SPP because of high prefetc acuracy and high prefetch coverage


++++ action pruning
+++ tweakble pythia through registers for  feature selection

---- would tuing the reward values together lead to better results?

+++ pythia evaluation using champsim

EVALUATIoN
incrases linerarly with number of cores
the less dram bandiwth, the better pythia performs in compairosn to MLOP, BINGO

--- multi-level prefetching schemes were not evaluated (pythia on L1, L2, L23

+++ customizion of feature selection and rewards (ie. focusing on NOT prefetch actions) Ligra workload suite

low area and power overheads (1%
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

84

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

5

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

3

==+== C. Paper summary

Non-volatile memories come with a drawback: it needs to ensure crash consistency as in the event of a crash, the memory operations could have not all been serviced (stores or writes). DRAM technologies do not suffer such issues as it when the power is turned off, it retains no data. In the case of NVMs, the system needs to be able to pick up where its last state was. Moreover, this partitioning between DRAM and NVMs imply a huge burden for the programmer which needs to design his program carefully, potentially leading to wrong types or access patterns.

Checkpointing is used to restore the microarchitectural and memory state in case of failure. It is a costly operation which depends on the granularity at which the data was saved as well as where (NVMs or DRAM) it is stored (access latency). ThyNVM reduces the stall time by overlapping the application execution and checkpoint time through the help of an OS-transparent hardware address space on the memory controller, that leverages both DRAM and NVM for efficient checkpointing. It employs two levels of granularity, at the cache block level and at a page granularity, which are stored on NVM and DRAM respectively.

ThyNVM is formally proven and has been evaluated on different access patterns against 4 other systems. It reduces NVM write traffic by 12% in average, while providing a performance increase against competitors due to the overlapping of runtime and consistency check.

==+== D. Comments for author

Section 4 is rather hard to follow and would necessitate additional illustrations to comprehend more easily (example, changing the notations). For instance, in 4.2 I understand that the mechanism to transfer from BTT to PTT happens at the beginning of an epoch. In 4.3 it is not mentioned how an entry is added into the PTT.

The store counter thresholds have been determined empirically, how does their value impact the bandwidth or performance (ie. doubling or halving).  other numbers (doubling or halving).

Overall, the three epochs mechanism is well designed as well as the  invisible partitioning for the software. A noticeable improvement is how few storage space it requires compared to logging-based methods.

Woulnd't it possible that there are multiple entries indexed at the same offset, so that hardware addresses collide (in BTT and PTT)?

You could also provide a graph which plots the NVM memory write bandwidth usage VS the stall time for ThyNVM.

Additional comments:
- In the figure 9, we can hardly distinguish ThyNVM from the others
- Figure 6 was a great addition

# Strength

- Two-granularity levels and clever synchronization system 
- Software transparent
- Scalable and improvements if we increase BTT size

# Weaknesses

- Source code and simulation setup not available anymore
- Loss of external states on system failures (ie. network card) anything that could be done in that regard?


==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Byte addressable non-volaitle memories (NVMs)
promise persistent memroy
need to guaranteee crash consistency
-> partition persistent and transient memroy data
2) use specialized software interface when updating memroy data

ThyNVM is a hardware assistes DRAM+NVM persistnet memory design
ThyNVM supports software transparent crash consistency of memory data in a hybrid memory system
dual scheme checkpointing time with application execution time

cehckpoint of data at multiple granularities in a coordinated manner
ThyNVM devises a software transparent mechanism to ensure crash consistency in persistent memory systems

goal -> reduce checkpointing time
1) overlaps checkpointing time with application exeecution time 
2) dynamically detemines checkpointing granularity of data by making the new observation of tradeoff between application stall time and metadata storage overhead of checpointing

reduces etadata sotrage overhead
and greatly increase effective memroy bandwidth utilization

-> manually partitionning is burdensome for the programmer
->reference between transient and persistent data in a unified memory space require careful management
->applications need to employ transaction to update persistent data


inefficiency of logging and copy on write (every memory update has to be logged.. and log replay increases the recovery time on system failure)

cehckpointing is a periodical update to NVM of memory data

checkpoint granulartiy is determined be granularity atwhich we keep track of the working/checkpoint data

checkpnt latency is affected by the location of he working copy of data (DRAM or NVRAM)

DESIGN
enforces cras consistency over all memory data transparently to application programs

sparse writes are checkpointed at cache block granularity, dense writes are checkpointed at page granularity

ASSUMPTIONS
failure model > periodic checkpoint of memroy data and CPU state 

epoch has an execution phase amd a checkpointing phase
alternating those two provide a significant performance boost

overlapping epochs to prevent stalls
1) isolate data updates of diferent epochs
2) maintain a safe copy of the active and last epoch

new working copy (for cache blocks) is mapped to a different address in NVM only persists the metadataneeded to locate the last checkpoint in the checkointing phase

page writeback is done on DRAM at page granualrity

dirty pages are written back to NVM only during checkpointing
ThyNVM directs each dirty page to a different address during checkpoingting
PTT tracks the address mappings for pages that are in DRAM

SCHEMES COORIDNATIONS
(switching between the two schemes)

IMPLEMENTATION
address space layout and management
physical address space is different from the memory controller's civew of the HW address space 

1) store different versions of data in different memorylocations in the hardware address space
2) expose a single consistent vesio of the data to the processor upong a load/store access or during system recovery

2 types of data:
- not affected by checpointing (not remapped by BTT/PTT)
- affected

software visible ddress space is not the same as controller's address space

BTT and PTT contain translation of the physical address of each memr req, streering of th dataupdates for checkpointing to appropriate HW address, determinationof when to migrate data between the two checpointing schemes

HW ADDrESS CAN COLLIDE (multiple entries at the same offset?)
store counter increment? how do you determine if you are targeting a single cache block or the whole page

SERVICING LOADS AND STORES

store req uses PTT to determine block remapping or page rite back
performs block remapping for all req that mis in the PTT


+++ figure 6 helpful

---source code and simulation setup not available anymore

EVALUATION
journaling
shadow paging (perf decr. due to full pages wrote back from DRAM to NVM)

adaptivity of ThyNVM to different access patterns reduces overall NVM write traffic across various patterns
2) by overapping eecution with checkpoiniting, thynvm reduces execution time but has more NVM write traffic

--Figure 9 cant see thynvm

BTT size increases trasaction troughput
Whole System Persistence model -> cpu and NVM only

--- Loss of external states on sstem failures (network card)

==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

87

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Deep Neural Network have a wide range of applications and there is an ever growing set of fields that are using them. Commodity hardware or specialized hardware are used to run them. Their workloads are highly memory intensive leading to vast energy-consumptions that often could be prevented due to the regenerative property of DNNs (error-resilient).

This paper EDEN presents a novel approach for a reduced energy waste by altering two important DRAM parameters: Voltage and Timings. Violating the normalized increase the bit-error rates in the DRAMs but DNNs can tolerate this noise due to their multi-layered structure. Retraining of the DNNs is performed on the modified DRAMs, so that their model plans ahead and accommodate to errors within a 1% tolerance goal. The DNN layers are mapped to different DRAMs partitions that have varying {voltage, timing} configuration, to set the error rate to an appropriate level for each layer.

EDEN has been tested on CPUs, GPUs, DNN accelerator and improve error resilience by x10, with an average of 25% energy reduction and a speedup of up to 8%.


==+== D. Comments for author

A huge positive aspect of EDEN is that it fits all DRAM models produced by any vendor. The well-thought-out procedure and the evaluation models prove that EDEN fits common DRAMs.

EDEN leverages a mechanism not previously applied to DNNs before, hopefully in the future DRAM vendors will not add a sub-voltage threshold stop mechanism to prevent such bit-errors from happening for security concerns.

Circular retraining is a clever way to let EDEN be permeable to errors and boost the DNN accuracy.

As you said, power is proportional to Vdd^2, so for a voltage reduction of 20%, we should see an energy efficiency improvement of 40%, which is not the case. Its not too far off but probably a section explaining the discrepancies could add some value.

# Strength

- Novel technique to reduce DNNs energy consumption
- Achieves sub <1% precision error
- Accuracy collapse defense
- Extensive characterization
- EDEN offloading, or offline EDEN training

# Weaknesses

- division of mapping onto the DRAM partitions, banks, subarrays: does a given layer have to have the same configuration?
- (does not work on reliable dram)

Additional comments:
- Figure 11. I suggest adding "tolerable" next to BER on the Y-axis
- Figure 13. any explanation on poor SqueezeNet energy reduction? or is it linked to the following section

-(side comment) lots of repetitions in the paper that make the read difficult ("we propose eden.."/in the background/eden explanation..),

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

EDEN
increasing memrozntensitz of most DNN workloads, goalis to use approximate memory ( violating timings and reduced supply voltage), leading to higher bit error rates

but neural netowwrk can tolerate increased bit errors

map the memroy error in in a DRAM partition in realation to user specified DNN accurayc requirements
evaluated on multi-core GPUs, DNN accelerators

EDEN DNN retraining improve error siliency by x10 with a 1% accuracy loss, average 25% energy reduction and a speedup (max of 8%..)

ISSUES
dram energy and latency 


approach of eden is to custimnize off-theshelf DRAM chips to better suit the DNN

EDEN 3 principles:
.retraining of DNN with the error tolerance of altered DRAM
.profiling of mproved DNN at all layers of the DNN
.map different DNN data to different DRAM partitions with different voltage and latency violation configuration

user defined accuarcy
---- repetitions of "we propose eden..."

BACKGROUND
Weight matrix, input feature maps, output feature maps
overparametrization is the source of DNNs accuracy
quantization of floating points weigths and OFM into fixed point can greatly improve energy and perforamce

Power is proportionnal to the square of supply voltage (vdd^2xf)

EDEN
1. boost DNN erreror tolearance
2. DNN error tolerance characteriuation
3. DNN DRAN mapping

1.circular reraining to boost DNN error tolerange, it injects the error into the DNN training procedure and boost the DNN accuracy

2. cahracterize IFMS, OFM and weights to identify the lmits of bi eror tolerance using the DNN validation dataset


1. accuracy collape, to provent this we derive slowly from the initial DRAM parameters to a target value , increase every two epoch seems to work relatively well

---- DOESNT NOT WORK ON RELIABLE DRAM

avoid accuracy collapse by not using values that are implausible

DNN error tolerance characterization
coarse grained characterization
logarithmic scale binary search on the error rates

coarse grained -> error tolerance
fine grained -> map highest tolerable bit error rate (BER) of each weight and map it  to a different DRAM portion

---maping of all a layer weight to the same DRAM partitions

EDEN OFFLAOADING
to train EDEN on a DNN without access to the DAM with an error model

chracterized DDR3 and DDR4 DRAM modules
errormodels
1.uniform random distribution across a DRAM bank of bt errors
2. bit errors follow a vertical distriution across the bitlines of a DRAM bank
3. horizontal distribution cross wordlines
4.uniform distrubtion that is data-dependent

model selection estimates a likelihood estimation procedure to determine the parameters of each error model and the error model that is most likely to produce the error

MEMORY CONTROLLER MODIFICATION
correct implausible values with upper and lower bound thresholds ( 1 cycle latency only)

RAm is split into 2^10 partitions 

EVALUATION
accuracy validation of the error model using differet numeric precisions
complete DRAM profiling can take 4 minutes

the way in wichc each error model captures the distribution of weak cells across data layout affects its imppacton the error curev

difference of accuracy across BER and quantization levels depending on the error model

VOLTAGE REDUCED BY 26% and trcd by 48%

----Figure 11. add "tolerable" next to BER

CPU-GPU

---Figure 13 . anyexplanation on poor SqueezeNet energy reduction?
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

88

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

3

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

1

==+== C. Paper summary

On-chip networks in todays' dies usually bound caches-to-caches or processor-to-cache for inter-communication. They represent approximately 30% of the power consumption: the performance/power ratio is a recurring issue in todays' designs. However, those networks tend to be on the lower-intensive spectrum edge in terms of usage. Can this property be exploited for less-energy consuming on-chip networks?

This paper introduces bufferless routing, saving (1) energy, (2) simplifying design and (3) providing similar performances to previously existing networks with buffer routing. The concept is simple: each router has the same number of inputs/outputs and the flits will constantly be on the move and never halted at any router.

The advantages are numerous: a simpler flow control, design area reduction, router latency reduction. Nevertheless, those are counterbalanced as it prevents different classes of traffics, can add latency to packets transmission (unpredictable), and also increases the buffer size on the receiver end. Overall, the performance degradation is less than 3% but there's up to 40% of saved. 

Future research in this bufferless direction will lead to more optimal algorithms that could substantially improve the results compared to this baseline. This paper is a solid groundwork for further improvements.

==+== D. Comments for author

You have thought a lot about the implications of removing the router buffers and how WORM should be adapted (ie. passing flits header next flits). Under the evaluation there could be a sub-section dedicated to the optimal size of receiving buffer. The synthetic traces validate the whole work that has been achieved in the paper and the baseline comparison were wisely chosen.

There is an assumption that all memory requests are hits which is the worst case scenario. Could adding delays to serve the memory requests remove some predictability in the network  it bandwidth intensive? The Matlab example doesn't seem very convincing as it highly depend on the memory pattern. More exploration on the cache-to-cache stress impact of memory latency is needed.

This might be because I am lacking knowledge in the field, but there is no background section which sometimes makes the decision process and the solutions harder to comprehend. A few examples where this could have proved useful: relation between packet and flits, flits header implication, link traversal, switch traversal, virtual channels..

Additional comments:

- 6.3 first paragraph, is it Vdd = 1.0 V, or each router is at VDD?

# Strength

- simple yet effective!
- Almost negligible performance degradation
- Room for exploration in bufferless algorithms

# Weaknesses

- No simulation of parallel applications
- Increased buffer size on the receiving end (not modeled?)
- Lacks a background section

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)
A Case for Bufferless Routing in On-Chip Networks

eliminating routing or flowcontrol in chip interconnect
reducs sign. the energz consumption
prodivdes similar performances

up to 40% power

input buffer occupz 75% of the on/chip network area
eliminate uffers in the desin of on/chi cache/to/cache and cache/to/memroz netowkr

bufferless routing is to alwazs output a packet wheter or not that reuslts in the smallest path
routed to anz portevalue practical buffreless routing algorithms and comare them against baseline buffered algo
--- only work with low cache miss rate?

reomving bffer is a reduction of the total available bandwitdhth in the network

1)energy reduction?
2) gap between BLESS saturation throughput and buffer satur. througp.
3)realistic situation in which an interconnection netwok is operated ata traffic injection ratebelow bless?
4) any benefts to removing buffers?

FLIT-BLESS
each flit of a packet is routed independently of every other flit through the network
flits for a same packets may take different path (traditionnaly, they would be stored in buffers)

network topology needs to satisfy: 
-eevery router has same nb of output ports as input ports (OP and IP)
-every router is reachable from every other router

assume mesh topology

injection policyat least one free output port
arabitration policy decides which incoming flit is routed to which output port
ranking component and a port selection component
arbiration policy is rank based
ranking of output port  is determined by its desirability for this flit

five different ranking policies have been evaluated

oldest first (OF) ranking ensure the oldest flit will be always delivered to its destination

WORM BLESS
flit-level switchng in flit bless has three disadvantages (not energy optimal, negative impact on packet latency)

additionnal head wire
packet is delayedby any late flits

worm bless is an optimization to flit bless 

only the first flit of each packet should ontain header information
subequent flits should simply follow he preceding flit

worm truncation
-> each router maintains an allocation of worms to output ports
once the head flit of a packet is routed to a specific output port, this port is allocadted to this worm until the tail flit of the wrom passe the output pport.

-> small table in the router that contains informationon which output port is aallocated to which worm

injection policy: worm in injected when not all IP are busy
a worm can be truncated when new rosm arrive on all 4 input ports
the second part of the worm is injected by its first flit becoemes a head flit

prioritiyation: to avoid livelocks

WORM blss save energy compared to FLIT bless bcause of the reductionoof header flits

BLESS WITH VUFFERS
not using any buffers has little impact on performance of real applications, and adding buffers to blesscan have benefits: it increasesthroughput and decreases latency for high injection rates
buffers reduce the probability of misrouting

REDUCTION OF ROUTER LATENCY
baseline router has a 3 stage pipeline: 1)buffer write and for head flit route computation
2)virtual channel allocation and switch allocation
3) ??

--- background about flits? link traversal ?


--eliminating virtual channels prevent difeerent classes of trfic 


ADVANTAGES
purely local and sipmple flow control
simplicity and router latency reduction
area saving
absence of deadlocks and livelock
adaptivitiy
congested areas packets will be deflected ayay from local hotspots

DISADVANTEGES
increased latency (cause the deflection will take a longer path)
increased buffereing at the receiver (flits of a paket  can arrive out of order and not in time)

interesting that flit bless tends to acheieve better performance than worm bless

injection rate are considered low

--- no simulation of parallel applications
-- 6.3 1.0 Vdd. 

does memroy hit necessarly reduce stress on the chip cache to cache network

very small performance degradation (less than 3%)

BLESS reduces network enegy considerably

buffer energy not defined
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

89

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

3

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

1

==+== C. Paper summary

(written in 2010)

Network on chip is a growing trend that interconnects a multitude of cores together. Packets are sent across the network and arbitration strategies (round-robin or oldest-priority) are employed to share critical resources. Multi-core dies popularity is going-up due to parallelized computing and we need to account for the upcoming bottleneck of packet transmission, which doesn't account for system performance. Hence the need to (1) classify packets by their application-criticalness, (2) find a convenient algorithm that gives room to fairness and (3) scale it to an arbitrary memory-sharing model and network size.

Aergia estimates the slack of each outgoing packets and classifies them with an order of priority determined by three metrics: number of hops to reach its destination, number of preceding L2 misses, and whether or not the new packet is a L2 miss or it. Arbitration and network interface use those priorities to speedup the most critical packets at a given time.

Their method focus and can be merged with parallelism-aware memory scheduling to reach even higher overall performance improvements.

==+== D. Comments for author

The slack quantization method is clearly efficient and grouping into batches is to prevent starvation is smart as well.

The presentation of the weighted sum (priority-bits) is lackluster, it needs a higher-level overview (figure?) to comprehend the "bin division" and how/where the packets are exactly being sorted.

Otherwise, it seems that it could be useful to put metrics on several additions that have been made: piggy-backing of the miss/hit to travelling packets, area overhead, energy consumption both to the router and network.

Figure 5. an explanation of "unfairness" and how you measure it would be helpful. It seems that STC and Aeria have approximately the same speedup, only combining them makes a little improvement.

# Strength

- Combinable to parallelism aware memory scheduling for further improvement
- Simple yet effective slack quantization method
- Angle of attack not touched upon by previous work

# Weaknesses

- Many self-references in the literature
- Code/ressources to reproduct non available which is an issue due to the rather short evaluation
- Short evaluation

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

Network on chip employs simple arbitration stategies such as round robin or oldest first, whch treat packets.

slack is a key measure for charaterizong a packet relative importance

aergia introduces new router prioritiyationpolicies that exploit interfering packets availableslack to improve overall system perforamnce and fairmess



arbitration poloci to teart allincoming  paackets and prioritize the output not depending on age or round robin fashino

AEGERIA
not all load miss cause bottlenecjs

packet slack = nb of cycles it can be delayed in the network withot affecting the application execution time

estimate available slack before transferring packet and

batch system to prevent startvation and atalling progress

MOTIVATION
run-ahead and out of order execution
MLP on on-chip network lead to packet latency overlap

accelerate packets with a small slack

SLACK estimation
local slack -> nb of cycles a packet can be delayed without delaying subsequent intructions
gloabl slack -> nb of cyclces a packet can be delayed without delaying the last instruction in the program

FOCUS ON LOCAL SLACK
consider slack only with respect to outstanding network transactions
predecessor packets for a packet P all the packets that are still outstanding and that have ben injected by te same ore into te network earlier than P

-- 1 could be #predecessors

key challenge is to estimate the slack
-> difficult to do
-> categoriye and quantize slack into different priority levels according to indrect metrics
-> most important factors are the nb of predecessors that are L2 hit or miss, nb of a pacet's extra hops in the network
-> relation between predecessors L2 miss to future slack
-> 3rd metric is nb of hops in the network

tagging of the packet ead wih priority bits 

every core maintains a list of outstanding L1 load misses

each L1 miss is associated with  a corresponding L2 miss status bit
control packets to send back L2 miss or hits to cores
piggy backing of the information to already travelling packets 

L2 miss or hit predictor in each core to guess injected packets cache hit miss status

-> global branch predictor
-> threshold predictor (misses occur inbursts)

NoC architecture
starvatuin avoidance (using batching) and mitigating priority inversion (multiplenetwork interface queues)

Baseline

Arbtration
aergia, virtual channel arbitration and swich arbitration units prioritize packets with lower slack priority levels.
low slack packets get preference for buffers and crossbar -> they are accelerated

packets from older batches are prioritized from the ones with younger batches

network interface is devided into sevaral equal length queue that store packets depenind on their priority

Network interface

Aergia optimizes system throughput by explotiing packet slack

+++ combinable to parallelism aware memry scheduling
==+== End Review
==+== Computer Architecture Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==+==" UNLESS DIRECTED!
==-== For further guidance, or to upload this file when you are done, go to:
==-== https://safari.ethz.ch/review/architecture21/offline

==+== =====================================================================
==+== Begin Review
==+== Reviewer: Guillaume Thivolet <gthivolet@student.ethz.ch>

==+== Paper Number

97

==+== Review Readiness
==-== Enter "Ready" if the review is ready for others to see:

Ready

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:

4

==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice:

2

==+== C. Paper summary

Multiprocessor systems are designed around low-cost microprocessors and share memories for the purpose. In a classical configuration, each processor is accompanied by its memory module. A network is in charge of interlinking every processor to any memory to allow for sharing. However, the cost of those networks exceed those of the multiprocessing system in itself. Such networks are especially tough to design when dealing with the general case of random memory accesses.

A delta networks is a simple cost-efficient synchronous network, that  approaches crossbar networks in terms of performances. It divides the interconnection into multiple stages that each route wires to different modules (demultiplexers), ultimately resulting in each end node being reachable by any processor.

The implementation and evaluation has been explored methodically under the same assumptions for both, and it results that the delta-2 network is competitive after a crossover point of network size 16.


==+== D. Comments for author

In the timeline in which the paper was published, it is a valuable asset to the network interconnect community. Overall this is a pleasant read that balances the probabilistic approach to the real-system design and the conclusion reached shows that delta-networks are useful for certain system configurations.

All the explanations were rather convenient to follow (ie. permutation deck) under the hypothesis formulated by the author, with the exception those could be invalidated in a real-system. For instance, the processor generates requests that are non-necessarily random (streaming/strided patterns), and this could lead to some memory being only vested to a single processor while degrading performance for others. Additionally, requests that are blocked are usually going to be sent again, which could lead to the same issue (congestion) mentioned right before.

A concluding table about the bandwidth reached by crossbar/delta networks and depending on b, n and N parameters would have been a more concise way than the graphs(Figure 11 to 14) to illustrate. Real numbers for the memory access time and gate delay could have been introduced for a more thorough evaluation.

I think that this arbitration method used in the paper doesn't account for request priorities and assumes an ideal random distribution of memory requests. Especially the control box that just prioritizes the R0, which could lead to R1 never being sent across a stage.

Lastly, it would have been fair to mention a possible asynchronous implementation for future work.

# Strength

- Formal probabilistic evaluation
- Simple yet almost cost-efficient alternative to crossbar networks
- Best link pattern is well explained
- Evaluation on a simple simple 2x2 case as well as a general b^n case
- Crossbar and delta evaluated under the same hypothesis (expection of gate delays)

# Weaknesses

- Unfair arbitration method
- Hypothesis rarely valid
- No asynchronous

==+== E. Comments for PC
==-== Hidden from authors.

==+== Scratchpad (for unsaved private notes)

A new class of interconnection networks for multiprocessing szstems
parallel tzpe processor 
share  single min memroz through interconnection network

time-shared bus has a very limited transfer rate
ful lcrossbar switch at the other spectrum end is the most expensive

DELTA NETWORKS
2x2 crossbar switch can connects input to any outputs (demultiplexer)

in a delta network, each module is controlled by a single digit from the destination adress
no external or global control is required
idenetity permutation at the same time is not possible

one and only one path is abailable from ane source to ay destination
2^12 permutaitons

1-by-8 demultiplexer

arbitration required for conflictinng requests by accepting some and rejecting others

it is a b^n x b^n network made up of nb^(n-1) switches, each being bxb crossbar switches

each superposition must satisfy two condtions
-> no more than b^n-1 modules may be used at any level and no mrore than n levels are created
-> each BxB module must have all its inputs connected to identically labeled outputs

large possibility of link patterns availalbe for a given delta network (is one topology better than another?)


low effectiveness for random memrpy accesses

uniqueness of a path between a source and a sdestination simplifies the control and analysis of delt networks

very clear permuation explanation

IMPLEEMNTATION OF DELTA NETWORKS

description of 2x2 modules

control box is to generate the signal X and provide arbitration 
Q request exists at an input port if he corresponding request line is 1.
all processors requiring memroy access must submit their requests at the same time bx placing a 1 on the respective request line


--snychronos implemetation is not preferable if the network has many staes (but costly)

ANALYSIS OF DELTA NETWORKS
analyzing b^nxb^^n
-> each processor generated random and independent requests and they are uniformly distriuted over all mem
->  mean request generation rate is 1 or 0
-< new requests are generated every ycle and submitted at the same time
-> requests which are blcked are ignored (to simplify analysis)

quantization of probabilitiy of acceptance of a request and the expected bandwdth of any 2^n x 2^n delta network givene a mean request generation rate ,

ANALYSIS of Full Crossbar Networks (comparision)
Figure 11. shows tht delta-2 and delta -4 become inneficient after a certain N 

a cycle for a crossbar could be smaller than a cycle for a large delta network. gate delay of delta network is higher than of crossbar. but memroy access time is considered 
==+== End Review

