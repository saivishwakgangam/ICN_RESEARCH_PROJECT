* Assume 5 contents and 10 edge nodes and a central server
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
* Modelling length(km) of coverage area of each Edge Node Matrix size will be [10*1]

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
Modelling Jam Density worst case(number of vehicles per km)
The matrix of size 10 \* 1 is:
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
Now modelling Available bandwidth between edge nodes and vehicles:
The matrix size will be 10 * 1
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
Now modelling transmission delay between an edge node and server
$$
t_{i,s} = \frac{Size_{c}}{100 \hspace{0.1cm} mbps}
$$
-------------------------------------------------




