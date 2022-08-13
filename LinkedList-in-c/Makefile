CC = gcc
CFLAGS = -Wall -pedantic -ansi -Werror
OBJ = list.o main.o
EXEC = run

$(EXEC) : $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

list.o : list.c head.h
	$(CC) -c list.c $(CFLAGS)

new.o  : new.c head.h
	$(CC) -c new.c $(CFLAGS)

clean:
	rm -f $(EXEC) $(OBJ)
