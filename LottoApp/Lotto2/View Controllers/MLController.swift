//
//  MLController.swift
//  Lotto2
//
//  Created by Swantewit on 18/09/2021.
//

import UIKit

class MLController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var mlResult: UILabel!
    
    func iterateNremove() -> (Set<Int>, Set<Int>){
        var nums = Set<Int>(1...42)
        var reslts = Set<Int>()
        for _ in 1...5{
            let randNum = nums.randomElement()!
            reslts.insert(randNum)
            nums.remove(randNum)
        }
    return (nums, reslts)
    }
    
    @IBAction func mlRand(_ sender: Any) {
        
        let it = iterateNremove()
        let res = it.1
        
        let mlStrng = res.map(String.init).joined(separator: ", ")
        
        mlResult.text = mlStrng
    }
    
    
    @IBAction func switchViews(_ sender: UIButton){
    }
    
    @IBAction func wroc(_ sender: Any) {
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
