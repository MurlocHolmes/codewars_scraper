"This time no story, no theory. The examples below show you how to write function `accum`:

**Examples:**

```swift
accum(\"abcd\") // -> \"A-Bb-Ccc-Dddd\"
accum(\"RqaEzty\") // -> \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum(\"cwAt\") // -> \"C-Ww-Aaa-Tttt\"
```

```fsharp
accum \"abcd\"    -- \"A-Bb-Ccc-Dddd\"
accum \"RqaEzty\" -- \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum \"cwAt\"    -- \"C-Ww-Aaa-Tttt\"
```

```clojure
(accum \"abcd\")    ; \"A-Bb-Ccc-Dddd\"
(accum \"RqaEzty\") ; \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
(accum \"cwAt\")    ; \"C-Ww-Aaa-Tttt\"
```
```coffeescript
accum \"abcd\"    # \"A-Bb-Ccc-Dddd\"
accum \"RqaEzty\" # \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum \"cwAt\"    # \"C-Ww-Aaa-Tttt\"
```
```cpp
Accumul::accum(\"abcd\");    // \"A-Bb-Ccc-Dddd\"
Accumul::accum(\"RqaEzty\"); // \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
Accumul::accum(\"cwAt\");    // \"C-Ww-Aaa-Tttt\"
```
```csharp
Accumul.Accum(\"abcd\");    // \"A-Bb-Ccc-Dddd\"
Accumul.Accum(\"RqaEzty\"); // \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
Accumul.Accum(\"cwAt\");    // \"C-Ww-Aaa-Tttt\"
```
```elixir
Mumbling.accum \"abcd\"    # \"A-Bb-Ccc-Dddd\"
Mumbling.accum \"RqaEzty\" # \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
Mumbling.accum \"cwAt\"    # \"C-Ww-Aaa-Tttt\"
```
```haskell
accum \"abcd\"    -- \"A-Bb-Ccc-Dddd\"
accum \"RqaEzty\" -- \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum \"cwAt\"    -- \"C-Ww-Aaa-Tttt\"
```
```java
Accumul.accum(\"abcd\");    // \"A-Bb-Ccc-Dddd\"
Accumul.accum(\"RqaEzty\"); // \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
Accumul.accum(\"cwAt\");    // \"C-Ww-Aaa-Tttt\"
```
```javascript
accum(\"abcd\");    // \"A-Bb-Ccc-Dddd\"
accum(\"RqaEzty\"); // \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum(\"cwAt\");    // \"C-Ww-Aaa-Tttt\"
```
```php
accum(\"abcd\");    // \"A-Bb-Ccc-Dddd\"
accum(\"RqaEzty\"); // \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum(\"cwAt\");    // \"C-Ww-Aaa-Tttt\"
```
```python
accum(\"abcd\")    # \"A-Bb-Ccc-Dddd\"
accum(\"RqaEzty\") # \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum(\"cwAt\")    # \"C-Ww-Aaa-Tttt\"
```
```ruby
accum(\"abcd\")    # \"A-Bb-Ccc-Dddd\"
accum(\"RqaEzty\") # \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum(\"cwAt\")    # \"C-Ww-Aaa-Tttt\"
```
```typescript
accum(\"abcd\");    // \"A-Bb-Ccc-Dddd\"
accum(\"RqaEzty\"); // \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"
accum(\"cwAt\");    // \"C-Ww-Aaa-Tttt\"
```

The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.
"