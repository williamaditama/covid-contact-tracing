# Contact Trail / Crowder: COVID Contact Tracing App

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


---
## Discrete Updates Equation
$$ y_{t+1} := x \times w(x, ys) + y(1 - w(x, ys)) + d $$  
$$ x_{t+1} := y \times h(x, y)  + x(1-h(x, y)) $$

## Multivariate Gaussian Equation

$$ f_{Z}(z) = \frac{1}{\sqrt{|det(\Sigma)|}} \frac{1}{(\sqrt{2\pi})^k} e^{-\frac{1}{2} (Z - \mu)^T\Sigma^{-1} (Z - \mu) } $$