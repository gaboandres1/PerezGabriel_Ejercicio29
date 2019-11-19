evolve_A.png evolve_B.png evolve_C.png evolve_D.png : grafica.py data3.dat data2.dat data1.dat data.dat FTCS.x
	python grafica.py
data3.dat : FTCS.x
	./FTCS.x 3 > data3.dat
data2.dat : FTCS.x
	./FTCS.x 2 > data2.dat
data1.dat : FTCS.x
	./FTCS.x 1 > data1.dat
data.dat : FTCS.x
	./FTCS.x 0 > data.dat
FTCS.x : FTCS.cpp
	g++ FTCS.cpp -o FTCS.x
	
clean :
	rm -r *.png *.dat *.x