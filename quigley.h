/*************************************************************************
 *
 * quigley.h
 *
 * This library adds functions helpful for testing and debugging the ORK,
 * as well as controlling any bonus hardware that edunham decides to build. 
 *
 * Released under the GNU GPL3.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * See https://github.com/edunham/Quigley for latest updates to this code.
 * 
 *************************************************************************/

#define Q 10
/* Note that the Q multiplier should be 1 if running on Quigley, 
 * 10 if using any other ORK. Quigley is a special child with a slow clock.
 */

void blinky(char x);

void setMotors(char l,char r);
