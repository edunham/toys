/*************************************************************************
 *
 * ORK library of bonus functions that I've written to make life easier.
 * 
 * Include quigley.h in your main.c file in order to use these functions.
 * 
 * Uses ORK Libraries copyright (C) 2011 OSURC, 
 *                released under the GNU LGPL3.
 *
 * Libraries available at: 
 *                http://oregonstate.edu/groups/osurc/
 *
 * For updates, see https://github.com/edunham/Quigley
 * 
 *************************************************************************/

void blinky(char x){
        /* Blink the built-in LED x times*/
        while(x>0){
                ledOn();
                _delay_ms(50*Q);
                ledOff();
                _delay_ms(70*Q);
                x--;
        }
}

void setMotors(char l,char r){ 
        setMotor(LeftMotor,l); 
        setMotor(RightMotor,r); 
}

	


