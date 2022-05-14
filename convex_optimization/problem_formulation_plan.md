## Mathematical Model Formulation
* Assume 5 contents and 10 edge nodes and a central server
* Assume 20 vehicles present in network
* Create a popularity array(size = 1*5)
* Popularity Matrix is:
$$
\begin{bmatrix}
0.1 & 0.3 & 0.4 & 0.1 & 0.1
\end{bmatrix}
$$
* Create a vector for average requests to each edge node (size = 10 * 1)
$$ 
\begin{bmatrix}
100 \\
50 \\
20 \\
40 \\
30 \\
12 \\
80\\
30 \\
20 \\
10
\end{bmatrix}
$$


------------------------------------------------
* Assumption is Equal Share Of Bandwidth between vehicles
* Modelling bandwidth 
1. edge node to vehicles bandwidth
2. edge node to edge node bandwidth
3. Edge Node to Cloud Server Bandwidth

----------------------------------------------
* Modelling length(km) of coverage area of each Edge 
* Node Matrix size will be [10*1]
$$
\begin{bmatrix}
10\\
20\\
5 \\
20\\
10\\
3 \\
5 \\
5 \\
8 \\
8
\end{bmatrix}
$$
---------------------------------------------
* Modelling Jam Density worst case(number of vehicles per km)
* The matrix of size 10 \* 1 is:
$$
\begin{bmatrix}
10\\
10\\
18\\
12\\
12\\
8\\
9\\
11\\
11\\
9
\end{bmatrix}
$$
---------------------------------------------------
* Now modelling Available bandwidth between edge nodes and vehicles:
* The matrix size will be 10 * 1
$$
\begin{bmatrix}
100\\
100\\
100\\
100\\
100\\
100\\
100\\
200\\
100\\
200
\end{bmatrix}
$$
--------------------------------------------
* Now modelling available bandwidth between two edge nodes
(matrix size is 10*10):
* Assume every connection is 100 Mbps
----------------------------------------------
* Now modelling available bandwidth between an edge node and server:
* Matrix size is 10*1 where edge node and a server has a dedicated link of 100 Mbps
----------------------------------------------------
* Now modelling the size of each file content-matrix size will be (1*5)
$$
\begin{bmatrix}
500 & 1000 & 1000 & 2000 & 1200
\end{bmatrix}
$$
---------------------------------------------------
* Now modelling the tranmission delay between edge node and vehicle when a file is requested.
    $$ t_{i,c} =  \frac{Size_{c}}{B_{i}/(Density_{i}*L_{i})}$$

 * $ t_{i,c}$ matrix is of size 10 * 5
-----------------------------------------------------
* Now modelling the transmission delay between two edge nodes
$$
t_{i,j,c} = \frac{Size_c}{100 \hspace{0.1cm} mbps}
$$
-----------------------------------------------
* Now modelling transmission delay between an edge node and server
$$
t_{i,s} = \frac{Size_{c}}{100 \hspace{0.1cm} mbps}
$$
-------------------------------------------------
* Introducing bandwidth and Mobility Constraints 
* Bandwidth Constraint:
* Assumption is every vehicle moves with constant velocity(2 m/sec)
* Minimum Data an edge node can serve 
$$
Data_{v,e}^{min} = \frac{B_{e}}{Density_{e}*velocity_{v}}
$$
* Bandwidth Constraint is:
$$
\forall e,c \hspace{0.1cm} X_{e,c}*size_{c} \leq Data_{v,e}
$$
--------------------------------------------------------
* Considering Max Service Processing Time for each edge node Matrix will be size (10*1):
$$
\begin{bmatrix}
5\\
2\\
7\\
10\\
14\\
12\\
19\\
15\\
13\\
19
\end{bmatrix}
$$
-----------------------------------------------------
* Considering Mobility Constraint:
* In Mobility Constraint We consider Jam Density, Velocity of car, Length Of Coverage Area, Bandwidth and Processing Service into consideration
$$
Data_{v,e}^{min} = \frac{B_e * (\,\frac{Length_{e}}{Velocity_{e}}-Processing_{e} )\,}{Density_{e}*Length_{e}}
$$
------------------------------------------------------
* As of now for mobility we consider minimum time in which a vehicle can be under a coverage area. 
$$
T_{v,e}^{min} = \frac{Length_e}{Velocity_{v}}  
$$
$ T_{v,e} $ -> Indicated Vehicle v in coverage area of edge node e. 

* Constraint : processing service time + data delivery time should be less than Time a vehicle be in coverage area. 










