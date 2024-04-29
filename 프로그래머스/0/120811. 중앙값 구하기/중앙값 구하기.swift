import Foundation

func solution(_ array:[Int]) -> Int {
    var sorted_array = array.sorted()
    var n = Int(ceil(Double(array.count / 2)))
    return sorted_array[n]
}