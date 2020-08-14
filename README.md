# Contact Trail / Crowder: COVID Contact Tracing App

### user table

| id  | risklevel| lat    | long   |
|:---:|:--------:|:------:|:------:|
|  0  |     1    |    1   |    0   |
|  1  |     0    |    1   |    0   |

### locations

| id  |      lat |   long | fn_type| risklevel  | st_dev |
|:---:|:--------:|:------:|:------:|:----------:|:------:|
|  0  |     1    |    1   |    0   |   0        |
|  1  |     0    |    1   |    0   |

## REST API
### New User
New user creation
* POST /new_user
* Body
```
{
    userID (string)
}
```
new_user(userid)

### Ping a Location & Get Risk Level
* POST /ping
* Body
 ```
 {
     userID (string),
     lat (double),
     long (double)
 }
 ```
* Return
```
{
    riskLevel (double [0, 1])
}
```
ping(userid, lat, long) -> double

### BONUS: Insert a new location into the server
* POST /new_location
* Body
```
{
    lat (double),
    long (double),
    fn_type (string),
    st_dev (double)
}
```
ping(lat, long, fn_type, st_dev)

---
## Discrete Updates Equation
if y < x:

$$ y_{t+1} := x \times w(x, ys) + y_{t}(1 - w(x, ys)) $$  

if x > y:

$$ x_{t+1} := y \times h(x, y)  + x(1-h(x, y))$$

w(x, ys)

*

## Multivariate Gaussian Equation

$$ f_{Z}(z) = \frac{1}{\sqrt{|det(\Sigma)|}} \frac{1}{(\sqrt{2\pi})^k} e^{-\frac{1}{2} (Z - \mu)^T\Sigma^{-1} (Z - \mu) } $$

## app dependencies
- william fill this in!!

## server dependencies
- Flask==1.1.1
- Flask-RESTful==0.3.8
