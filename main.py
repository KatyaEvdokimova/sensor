import matplotlib.pylab as plt
import matplotlib.animation as animation
import array as arr
import numpy as np
import math

n=0
file_path = 'C:/Users/Екатерина/Desktop/shar.txt'

# Чтение данных из файла
y = np.loadtxt(file_path, dtype=int)
fig=plt.figure()

x = []
x_ball=[]
y_ball=[]
delta_x=0.1 # переменная, устанавливающая шаг по оси Ox
delta_t=0.1
resistance=0.09 # коэффициент сопротивления
g=10 # ускорение свободного падения
for n in range(len(y)):# создание массива X с шагом 2
 x.append(int (2*n))

temp_x= float(input("Введите координату х: "))
if(temp_x<=0 or temp_x>=200):
 print("Ошибка:выход за пределы графика")
 exit(0)

def find_y(temp_x):
 x0=int (round(temp_x-0.5))# нахождение ближайшего целого числа к введенной координате temp_x
 if x0%2!=0:               # проверка: является ли x0 нечетным числом
  x0=x0-1
 if x0<2*(len(x)-1) and x0>=0: # проверка: находится ли x0 в пределах допустимого диапазона для доступа к массиву y
  y0=y[x0//2]                   # получается значение y0 из массива y
  y1=y[x0//2+1]
  return (float (y0-(y0-y1)*(temp_x-x0)/2))# вычисляется значение вертикальной координаты y
temp_y=find_y(temp_x)
energy=g*find_y(temp_x)

def move1(now_x, now_speed):
    now_y = find_y(now_x)
    a = g * (find_y(now_x) - find_y(now_x + delta_x)) / pow(pow(find_y(now_x) - find_y(now_x + delta_x), 2) + pow(delta_x, 2), 0.5) # вычисляется ускорение a по формуле движения с постоянным ускорением, используя разницу в вертикальных координатах между текущим положением и следующим положением (find_y(now_x + delta_x)), а также шаг delta_x
    speed = now_speed + a * delta_t
    s = speed * delta_t # вычисляется перемещение s объекта за текущий временной шаг.
    next_x = now_x + s / pow(((pow((find_y(now_x + delta_x) - find_y(now_x)) / delta_x, 2)) + 1), 0.5)
    speed -= s * resistance # уменьшается скорость с учетом сопротивления.
    next_y = find_y(next_x)
    x_ball.append(next_x)
    y_ball.append(next_y)
    return (next_x, speed)


def init():
 redDot.set_data([],[])
 return redDot,

i = 0


def animate(i):
    #if(i>=len(x_ball)):
    # exit(0)
    redDot.set_data(x_ball[i], y_ball[i])
    return redDot,



def plot_ball():
   now_x=temp_x
   speed=0
   x_ball.append(temp_x)
   y_ball.append(temp_y)
   while(abs(speed)>=2 or (find_y(now_x+delta_x)-find_y(now_x))/delta_x!=0):
    (now_x,speed)=move1(now_x,speed)

plot_ball()

scale = 1.5
ax = plt.axes(xlim=(0,288),ylim=(0,183))

pit = ax.plot(x, y, 'k')
pit = ax.grid()
plt.ylabel('Ось У[мм]')
plt.xlabel('Ось Х[мм]')
plt.title('Движение шарика по кривой')
redDot, = ax.plot([0], [0], 'co')

ani = animation.FuncAnimation(fig, animate, init_func=init, interval=10, blit=True, repeat=True, save_count=len(x_ball))

plt.show()
