import Foundation

func solution(_ strlist:[String]) -> [Int] {
    var arr:[Int] = []
    for word in strlist {
        arr.append(word.count)
    }
    return arr
}