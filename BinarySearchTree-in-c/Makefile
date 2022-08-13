CC = gcc
OBJ = bst.o main.o extra.o
EXEC = bstTest

$(EXEC) : $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

main.o : main.c bst.h extra.h
	$(CC) -c main.c

bst.o : bst.c bst.h extra.h
	$(CC) -c bst.c

extra.o : extra.c extra.h
	$(CC) -c extra.c

clean:
	rm -f $(EXEC) $(OBJ)
