import Foundation

func solution(_ price:Int) -> Int {
    var pay:Int = 1
    switch price {
        case 500000...1000000:
        pay = Int(Double(price) * Double(0.80))
        case 300000...499999:
        pay = Int(Double(price) * Double(0.90))
        case 100000...299999:
        pay = Int(Double(price) * Double(0.95))
        default:
        pay = price
    }
    return pay
}