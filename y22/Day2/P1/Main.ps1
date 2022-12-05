$inputFile = Get-Content C:\\Users\\ericm\\Desktop\\AdventOfCode\\y22\\Day2\\input.txt

$total = 0

function getPoint {
    param ($choice)
    if ($choice -eq 'X') {
        return 1
    } elseif ($choice -eq 'Y') {
        return 2
    } else {
        return 3
    }
}

foreach($line in $inputFile.split("\n")) {
    $p = $line.ToCharArray()[0]
    $m = $line.ToCharArray()[2]

    $total += getPoint($m)
    if (($p -eq 'A' -and $m -eq 'X') -or ($p -eq 'B' -and $m -eq 'Y') -or ($p -eq 'C' -and $m -eq 'Z')) {
        $total += 3
    } elseif (($p -eq 'A' -and $m -eq 'Y') -or ($p -eq 'B' -and $m -eq 'Z') -or ($p -eq 'C' -and $m -eq 'X')) {
        $total += 6
    }
}

$total