$inputFile = Get-Content C:\\Users\\ericm\\Desktop\\AdventOfCode\\y22\\Day1\\input.txt

$lines = $inputFile.Split("\n")

$elfInventory = @()

$total = 0

for($i = 0; $i -lt $lines.length; $i++){
    $currentLine = $lines[$i]

    if ($currentLine) {
        [int]$value = $currentLine
        $total += $value
    } else {
        $elfInventory += @($total)
        $total = 0
    }
}

($elfInventory | Measure -Maximum).Maximum
