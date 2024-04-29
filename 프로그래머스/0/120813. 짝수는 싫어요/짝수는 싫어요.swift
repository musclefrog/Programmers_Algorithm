import Foundation

func solution(_ n:Int) -> [Int] {
    var result:[Int] = []
    for i in 0...n {
        if i % 2 == 1 {
            result.append(i)
        }
    }
    return result
}