grafica.png : data.dat FTCS.x grafica.py
	python grafica.py
data.dat : FTCS.x
	./FTCS.x > data.dat
FTCS.x : FTCS.cpp
	g++ FTCS.cpp -o FTCS.x
	
clean :
	rm -r *.png *.dat *.x