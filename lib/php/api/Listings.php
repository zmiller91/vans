<?php

/**
 * @author zmiller
 */
class Listings extends Service {
    
    protected function allowableMethods() {
        return array(self::GET);
    }

    protected function authorize() {
        return true;
    }

    protected function validate() {
        return true;
    }

    protected function get() {
        $ListingsTable = new ListingsTable($this->m_oConnection);
        $this->m_mData = $ListingsTable->select($this->m_aInput);
        return true;
    }
}
