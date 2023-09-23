defmodule PrimeFinder do
  def is_prime(num) when num <= 1, do: false
  def is_prime(2), do: true
  def is_prime(num) do
    num = round(num)
    Enum.all?(2..round(:math.sqrt(num)), fn i ->
      rem(num, i) != 0
    end)
  end

  def main do
    IO.puts("Enter a number (n): ")
    n = String.to_integer(IO.gets(""))

    IO.puts("Prime numbers up to #{n} are:")

    Enum.reduce_while(2..n, [], fn num, primes ->
      if is_prime(num) do
        {:cont, [num | primes]}
      else
        {:cont, primes}
      end
    end)
    |> Enum.reverse()
    |> Enum.each(&IO.puts(&1))

    IO.puts()
  end
end

PrimeFinder.main()
